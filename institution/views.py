from django.shortcuts import render,redirect
from company.models import CompanyInfo,Balance,Profit,CashFlow,FinancialSituation,EvaluationOfEnterprises,IndependentEvaluationOfEnterprises,get_user_group
from company.admin import CompanyInfoAdmin
from django.db.models import Max,Min,Count
from .models import *
from django.http import HttpResponseRedirect
from .admin import *
from django.contrib import admin

# Create your views here.
# 
# 
# 
# 
def investreport_view(request):
    if get_user_group(request,'机构用户'):
        return InvestReportAdmin(InvestReport,admin.AdminSite()).changelist_view(request)
    return HttpResponseRedirect('/admin/institution/report/')




def bankreport_view(request):
    if get_user_group(request,'机构用户'):
        return BankReportAdmin(BankReport,admin.AdminSite()).changelist_view(request)
    return HttpResponseRedirect('/admin/institution/report/')

def report_companyinfo_view(request,_type,num):
    num = int(num)
    _id = CompanyInfo.objects.get(**{_type+'__id':num}).id
    
    res = CompanyInfoAdmin(CompanyInfo,admin.AdminSite()).change_view(request,str(_id))
    
    # print('/admin/company/companyinfo/%s' % _id)
    # from pprint import pprint
    # print(res)
    # pprint(dir(res))
    return res

def createcompanyreport_view(request):
    if request.method == 'POST':
        cid = request.POST['cid']
        opt = request.POST['opt']
        _type = request.POST['type']

        modleName = 'investreport' if _type == '0' else 'bankreport'
        if opt == '最新年份' or opt == '全部年份':
            data = {}
            Report = InvestReport if _type == '0' else BankReport
            

            data['companyInfo'] = CompanyInfo.objects.get(id=cid)
            g = GetData(data['companyInfo'])


            g.maxyear -= 1
            before_fincome = g.fincome
            before_fprofit = g.fprofit
            g.maxyear += 1

            datakey = [3,3,0.85,0.05,0.1,
                        0.05,0.1,0.12,0.1,0.5,
                        1.5,2,2.5,0.015]
            datadict = { 'i%s' % i : n    for i,n in enumerate(datakey,5)}

            eoe = EvaluationOfEnterprises.objects.get(companyInfo=data['companyInfo'])
            try:
                data['i5'] = g.pc7 * 2 /(g.bd8+g.bd9+g.be8+g.be9)
            except ZeroDivisionError:
                data['i5'] = 0
            try:
                data['i6'] = g.pc11 * 2 / (g.bd14 + g.be14)
            except ZeroDivisionError:
                data['i6'] = 0
            try:
                data['i7'] = g.pc7 * 2 / (g.bd38 + g.be38)
            except ZeroDivisionError:
                data['i7'] = 0
            try:
                data['i8'] = (g.fprofit - before_fprofit) / before_fprofit
            except ZeroDivisionError:
                data['i8'] = 0
            try:
                data['i9'] = (g.bh28-g.bd38 + g.be38-g.bi28)/(-g.bh28 + g.bd38)
            except ZeroDivisionError:
                data['i9'] = 0
            try:
                data['i10'] =  (g.fincome - before_fincome)/before_fincome
            except ZeroDivisionError:
                data['i10'] = 0
            try:
                data['i11'] = g.pc30/g.pc7
            except ZeroDivisionError:
                data['i11'] = 0
            try:
                data['i12'] = (g.cd33 + g.pc28) * 2 / (g.bd38 + g.be38)
            except ZeroDivisionError:
                data['i12'] = 0
            try:
                data['i13'] = g.pc30 * 2 / (g.bh28-g.bd38 + g.be38-g.bi28)
            except ZeroDivisionError:
                data['i13'] = 0
            try:
                data['i14'] = g.bi28 / g.be38
            except ZeroDivisionError:
                data['i14'] = 0
            try:
                data['i15'] = g.cd9 / g.bi18
            except ZeroDivisionError:
                data['i15'] = 0
            try:
                data['i16'] = g.be17 / g.bi18
            except ZeroDivisionError:
                data['i16'] = 0
            try:
                data['i17'] = (g.pc28 + g.pc17) / g.pc17
            except ZeroDivisionError:
                data['i17'] = 0
            try:
                data['i18'] = g.fr_d_cost / g.fincome
            except ZeroDivisionError:
                data['i18'] = 0

            for key in data:
                if key == 'companyInfo':
                    continue
                data[key] = 1 if data[key] >= datadict[key] else 0
            data['i1'] = eoe.external_environment
            data['i2'] = eoe.products_and_market
            data['i3'] = eoe.technology_R_D
            data['i4'] = eoe.team
            _id = Report.objects.create(**data).id
            return HttpResponseRedirect('/admin/institution/%s/%s'%(modleName,_id))
        else:
            return HttpResponseRedirect('/admin/institution/%s/%s'%(modleName,opt))
        # return Admin(Report,admin.AdminSite()).change_view(request,_id)

class GetData(object):
    clss = {'b':Balance,'p':Profit,'c':CashFlow,'f':FinancialSituation}
    datadict_key = {
        'be38':'e24,-e25,-e27,e29,e32,e34,e36,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16',
        'bd38':'d24,-d25,-d27,d29,d32,d34,d36,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16',
        'bh28':'h6,h7,h8,h9,h10,h11,h12,h13,h14,h15,h16,h17,h19,h20,h21,h22,h23,h24,h25,h26',
        'bi28':'i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17,i19,i20,i21,i22,i23,i24,i25,i26',
        'pc30':'c7,c8,-c11,-c12,-c13,-c14,-c15,-c17,-c19,-c20,-c21,c24,-c26,-c29',
        'bi18':'i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17',
        'be17':'e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16',
        'pc28':'c7,c8,-c11,-c12,-c13,-c14,-c15,-c17,-c19,-c20,-c21,c24,-c26',
    }
    

    # minyear = min(Balance.objects.annotate(Min('year')),Profit.objects.annotate(Min('year')),CashFlow.objects.annotate(Min('year')))
    def __init__(self,companyInfo):
        self.companyInfo = companyInfo
        self.datadict = {}
        self.maxyear = max(
            Balance.objects.all().filter(companyInfo=self.companyInfo).annotate(Max('year'))[0].year,
            Profit.objects.all().filter(companyInfo=self.companyInfo).annotate(Max('year'))[0].year,
            CashFlow.objects.all().filter(companyInfo=self.companyInfo).annotate(Max('year'))[0].year,
            )

    def __getattr__(self,name):
        # if name in ['companyInfo','clss',]:
        #     return getattr(self,name)
        if name in self.datadict_key:
            if not self.datadict.get(name) is None:
                return self.datadict[name]
            self.datadict[name] = 0
            for key in self.datadict_key[name].split(','):
                fh = 1
                if key[0] == '-':
                    fh = -1
                    key = key[1:]
                self.datadict[name] += fh * getattr(self,name[0]+key)
            return self.datadict[name]
        elif name in ['fincome','fprofit','ftotal','fr_d_cost']:
            CLS = self.clss['f']
            try:
                data = getattr(CLS.objects.get(year=self.maxyear,companyInfo=self.companyInfo),name[1:])
            except CLS.DoesNotExist:
                data = 0
            return data

        CLS = self.clss[name[0]]
        try:
            data = CLS.objects.get(year=self.maxyear,companyInfo=self.companyInfo,name=name[1:]).value
        except CLS.DoesNotExist:
            data = 0

        setattr(self,name,data)
        return data

        
def report_view(request):
    return CompanyInfoReportAdmin(CompanyInfo,admin.AdminSite()).changelist_view(request)


def save_reportback_view(request):
    # print(request.POST)
    need_data = ['type','note','will']
    dic = {  da:request.POST[da]    for da in request.POST if da in need_data}
    obj = ReportBack(**dic)


    _id = request.POST['report_id']
    if request.POST['report_type'] == 'investreport':
        obj.investreport = InvestReport.objects.get(id=_id)
        obj.investreport.companyInfo.status = 9
        obj.investreport.companyInfo.save()
        CompanyStatus.create(companyInfo=obj.investreport.companyInfo,status=9)
    elif request.POST['report_type'] == 'bankreport':
        obj.bankreport = BankReport.objects.get(id=_id)
        obj.bankreport.companyInfo.status = 9
        obj.bankreport.companyInfo.save()
        CompanyStatus.create(companyInfo=obj.bankreport.companyInfo,status=9)
    else:
        raise ValueError('错误的数据:' + request.POST['report_type'])

    obj.institution = Institution.objects.get(user=request.user)
    obj.save()
    return ReportBackAdmin(ReportBack,admin.AdminSite()).change_view(request,str(obj.id))











# def test():
#     from django.utils.timezone import now, timedelta
#     date = now().date() + timedelta(days=-5) #今天
#     obj = BankReport.objects.filter(create_date__gte=date).values('create_date','companyInfo').annotate(conc = Count('create_date'))
#     print(obj)
#     for o in obj:
#         print(o.conc)
#     print(1111111111111111)

# test()