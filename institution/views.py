from django.shortcuts import render,redirect
from company.models import * #CompanyInfo,Balance,Profit,CashFlow,FinancialSituation,EvaluationOfEnterprises,IndependentEvaluationOfEnterprises,get_user_group
from company.admin import CompanyInfoAdmin
from django.db.models import Max,Min,Count
from incubator.models import Incubator
from .models import *
from django.http import HttpResponseRedirect
from .admin import *
from django.contrib import admin
from functools import reduce

# Create your views here.
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

def copy_company(cobj):

    

    # 删除 'companyInfo_id','id' companyInfo=cobj 来查找其他的
    # 复制company 需要删除 'user_id', 'id', 'incubator_id'

    del_company_fields = ('user_id', 'id', 'incubator_id')
    del_other_fields = ('companyInfo_id','id')

    # 需要清空的 平台管理员重新设置状态
    clschanges = (CompanyStatus,)

    # 需要复制的
    clscopys = (RejectReason,Shareholder,EnterpriseAwards,PersonalAwards,
            Project,Patent,DrugApproval,MIRC,StandardSetting,Otherm,CoreMember,
            FinancialSituation,ProductsAndMarket,TechnologyRD,ServerRequest,
            IndependentEvaluationOfEnterprises,EvaluationOfEnterprises,
            PTOfEnterprises,Bonus,Subtraction)

    # 不进行处理的 也可以进行复制
    clsnones = (Balance,Profit,CashFlow)

    companydict = CompanyInfo.objects.filter(id=cobj.id).values()[0]
    incubator_id = companydict['incubator_id']
    for field in del_company_fields:
        del companydict[field]
    companydict['incubator'] = Incubator.objects.get(id=incubator_id) 
    newcobj = CompanyInfo.objects.create(**companydict)

    for clscopy in clscopys:
        objs = clscopy.objects.filter(companyInfo=cobj)
        for obj in objs:
            objdict = clscopy.objects.filter(id=obj.id).values()[0]
            for field in del_other_fields:
                del objdict[field]
            objdict['companyInfo'] = newcobj
            clscopy.objects.create(**objdict)
    return newcobj
# x = CompanyInfo.objects.all().order_by('-id')[0]
# copy_company(x)

def createcompanyreport_view(request):
    if request.method == 'POST':
        cid = request.POST['cid']
        opt = request.POST['opt']
        _type = request.POST['type']

        modleName = 'investreport' if _type == '0' else 'bankreport'
        if opt == '生成报告':
            
            Report = InvestReport if _type == '0' else BankReport
            

            
            cobj = CompanyInfo.objects.get(id=cid)
            g = GetData(cobj)

            datakey = [3,3,0.85,0.05,0.1,
                        0.05,0.1,0.12,0.1,0.5,
                        1.5,2,2.5,0.015]
            datadict = { 'i%s' % i : n    for i,n in enumerate(datakey,5)}

            das = []
            for year in g.years:
                g.year = year
                da = {}
                try:
                    da['i5'] = g.pd7 * 2 /(g.bd8+g.bd9+g.be8+g.be9)
                except ZeroDivisionError:
                    da['i5'] = 0
                try:
                    da['i6'] = g.pd11 * 2 / (g.bd14 + g.be14)
                except ZeroDivisionError:
                    da['i6'] = 0
                try:
                    da['i7'] = g.pd7 * 2 / (g.bd38 + g.be38)
                except ZeroDivisionError:
                    da['i7'] = 0
                try:
                    da['i8'] = (g.pd31 - g.pc31) / g.pc31
                except ZeroDivisionError:
                    da['i8'] = 0
                try:
                    da['i9'] = (g.bi35-g.bh35)/g.bh35
                except ZeroDivisionError:
                    da['i9'] = 0
                try:
                    da['i10'] =  (g.pd7 - g.pc7)/g.pc7
                except ZeroDivisionError:
                    da['i10'] = 0
                try:
                    da['i11'] = g.pd31/g.pd7
                except ZeroDivisionError:
                    da['i11'] = 0
                try:
                    da['i12'] = (g.pd29 + g.pd18) * 2 / (g.bd38 + g.be38)
                except ZeroDivisionError:
                    da['i12'] = 0
                try:
                    da['i13'] = g.pd31 * 2 / (g.bh35+g.bi35)
                except ZeroDivisionError:
                    da['i13'] = 0
                try:
                    da['i14'] = g.bi28 / g.be38
                except ZeroDivisionError:
                    da['i14'] = 0
                try:
                    da['i15'] = g.cd15 *2 / (g.bh5+g.bi5)
                except ZeroDivisionError:
                    da['i15'] = 0
                try:
                    da['i16'] = g.be17 / g.bi18
                except ZeroDivisionError:
                    da['i16'] = 0
                try:
                    da['i17'] = (g.pc29 + g.pc17) / g.pc17
                except ZeroDivisionError:
                    da['i17'] = 0
                try:
                    da['i18'] = g.fr_d_cost / (g.pd7 - g.pc7)
                except ZeroDivisionError:
                    da['i18'] = 0

                for key in da:
                    if key == 'companyInfo':
                        continue
                    if key == 'i14':
                        da[key] = 1 if da[key] <= datadict[key] else 0
                    else:
                        da[key] = 1 if da[key] >= datadict[key] else 0
                das.append(da)

            def setda(x,y):
                res = {}
                for name,i in x.items():
                    res[name] = str(i) + str(y[name])
                return res


            data = reduce(setda,das)


            def getdata_data(i):
                if i in ['i1','i2','i3','i4']:
                    return data[i]

                di = data[i]
                if type(di) == int:
                    return di
                return int(data[i][0])


            eoe = EvaluationOfEnterprises.objects.get(companyInfo=cobj)
            data['i1'] = eoe.external_environment
            data['i2'] = eoe.products_and_market
            data['i3'] = eoe.technology_R_D
            data['i4'] = eoe.team



            bonus = Bonus.objects.filter(companyInfo=cobj).values('value')
            bonus = sum([ int(b['value']) for b in bonus])
            data['bonus'] = bonus

            subtraction = Subtraction.objects.filter(companyInfo=cobj).values('value')
            subtraction = sum([ -abs(int(b['value'])) for b in subtraction])
            data['subtraction'] = subtraction
            years = g.years
            years = [str(year) for year in years]
            data['years'] = '_'.join(years)


            if _type == '0':
                totle = (getdata_data('i1') + getdata_data('i2') + getdata_data('i3') + getdata_data('i4') *2) * 2 * 0.35 + (
                    getdata_data('i5') *10 +getdata_data('i6') *7 +getdata_data('i7') *8 +getdata_data('i8') *10 +getdata_data('i9') *5 +getdata_data('i10') *10 +
                    getdata_data('i11') *10 +getdata_data('i12') *5 +getdata_data('i13') *5 +getdata_data('i14') *5 +getdata_data('i15') *5 +getdata_data('i16') *5 +
                    getdata_data('i17') *5 +getdata_data('i18') *10) * 0.65
            else:
                totle = (getdata_data('i1') + getdata_data('i2') + getdata_data('i3') + getdata_data('i4') *2) * 2 * 0.35 + (
                    getdata_data('i5') *5 +getdata_data('i6') *5 +getdata_data('i7') *5 +getdata_data('i8') *10 +getdata_data('i9') *5 +getdata_data('i10') *5 +
                    getdata_data('i11') *10 +getdata_data('i12') *5 +getdata_data('i13') *5 +getdata_data('i14') *10 +getdata_data('i15') *10 +getdata_data('i16') *7 +
                    getdata_data('i17') *8 +getdata_data('i18') *10) * 0.65
            
            totle = round(totle + bonus + subtraction,2)
            data['totle'] = totle



            data['companyInfo'] = cobj




            zp = IndependentEvaluationOfEnterprises.objects.get(companyInfo=cobj)
            data['zp1'] = zp.external_environment
            data['zp2'] = zp.products_and_market
            data['zp3'] = zp.technology_R_D
            data['zp4'] = zp.team

            pt = PTOfEnterprises.objects.get(companyInfo=cobj)
            data['pt1'] = pt.external_environment
            data['pt2'] = pt.products_and_market
            data['pt3'] = pt.technology_R_D
            data['pt4'] = pt.team

            data['companyInfo'] = copy_company(cobj)

            _id = Report.objects.create(**data).id
            return HttpResponseRedirect('/admin/institution/%s'%modleName)
        else:
            return HttpResponseRedirect('/admin/institution/%s'%modleName)
        # return Admin(Report,admin.AdminSite()).change_view(request,_id)

class GetData(object):
    clss = {'b':Balance,'p':Profit,'c':CashFlow,'f':FinancialSituation}
    datadict_key = {
        'be38':'e24,-e25,-e27,e29,e32,e34,e36,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16',
        'bd38':'d24,-d25,-d27,d29,d32,d34,d36,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16',
        'bi28':'i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17,i19,i20,i21,i22,i23,i24,i25,i26',
        'pc31':'c7,c8,-c11,-c12,-c13,-c14,-c15,-c17,-c20,-c21,-c22,c25,-c27,-c30',
        'pd31':'d7,d8,-d11,-d12,-d13,-d14,-d15,-d17,-d20,-d21,-d22,d25,-d27,-d30',
        'bi18':'i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17',
        'be17':'e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16',
        'pd29':'d7,d8,-d11,-d12,-d13,-d14,-d15,-d17,-d20,-d21,-d22,d25,-d27',
        'bh35':'h30,h31,-h32,h33,h34',
        'bi35':'i30,i31,-i32,i33,i34',
    }
    

    # minyear = min(Balance.objects.annotate(Min('year')),Profit.objects.annotate(Min('year')),CashFlow.objects.annotate(Min('year')))
    def __init__(self,companyInfo):
        self.companyInfo = companyInfo
        self.datadict = {}


        yearsets = []
        for ob in [Balance,CashFlow,Profit]:
            yearset = [ o['year'] for o in ob.objects.all().filter(companyInfo=companyInfo).values('year').annotate(Count('year'))]
            yearset = set(yearset)
            yearsets.append(yearset)
        # print(yearsets)
        yearset = reduce(lambda x,y:x&y,yearsets)

        yearset = sorted(yearset,key=lambda x:x,reverse=True)[:5]
        self.years = yearset

        self.year = None

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
                data = getattr(CLS.objects.get(year=self.year,companyInfo=self.companyInfo),name[1:])
            except CLS.DoesNotExist:
                data = 0
            return data

        CLS = self.clss[name[0]]
        try:
            data = CLS.objects.get(year=self.year,companyInfo=self.companyInfo,name=name[1:]).value
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
        cobj = CompanyInfo.objects.get(name=obj.investreport.companyInfo.name,user__id__gt=0) 


        cobj.status = 9
        cobj.save()
        CompanyStatus.objects.create(companyInfo=cobj,status=9)
    elif request.POST['report_type'] == 'bankreport':
        obj.bankreport = BankReport.objects.get(id=_id)
        cobj = CompanyInfo.objects.get(name=obj.bankreport.companyInfo.name,user__id__gt=0) 
        cobj.status = 9
        cobj.save()
        CompanyStatus.objects.create(companyInfo=cobj,status=9)
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