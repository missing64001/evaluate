from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
# Create your views here.
from django.contrib import auth
from django.contrib.auth.models import User,Group
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from .models import *
from pprint import pprint
from django.db.models import F,Count
from django.contrib import admin
from .admin import IndependentEvaluationOfEnterprisesAdmin,EvaluationOfEnterprisesAdmin,CompanyInfoAdmin
from django.contrib import messages
import os
# 用户注册
# 
# 

def company_status_view(request):


    
    cobj = CompanyInfo.objects.get(user=request.user)
    status = cobj.status



    #设置 状态栏
    status_pic = ['finished','finished','finished','finished','finished']
    status_text = ['企业进度已完成','孵化器进度已完成','平台进度已完成','投资机构进度已完成','企业收到反馈信息']
    status_line = [''] * 4

    if status < 10:
        status_pic[4] = 'wait'
        status_text[4] = '等待平台发送反馈信息'
    if status < 9:
        status_pic[4] = '5'
        status_pic[3] = 'wait'

        status_text[4] = '企业未收到反馈信息'
        status_text[3] = '等待投资机构反馈给平台'

        status_line[3] = '_grap'
    if status < 8:
        status_pic[3] = '4'
        status_pic[2] = 'wait'

        status_text[3] = '投资机构进度未开始'
        status_text[2] = '平台发送评估报告到机构'

        status_line[2] = '_grap'
    if status < 7:
        status_pic[2] = '3'
        status_pic[1] = 'wait'

        status_text[2] = '平台进度未开始'
        status_text[1] = '所属孵化器审核企业信息'

        status_line[1] = '_grap'
    if status == 5:


        status_pic[0] = 'wait'
        status_text[0] = '企业提交信息'
        status_text[1] = '所属孵化器驳回企业信息'


    if status < 4:
        status_pic[1] = '2'
        status_pic[0] = 'wait'

        status_text[1] = '孵化器进度未开始'
        status_text[0] = '企业提交信息'

        status_line[0] = '_grap'

    if status == 2:
        status_text[0] = '企业进行自主评价'
    if status == 1:
        status_text[0] = '企业上传财务报表'
    if status == 0:
        status_text[0] = '企业填写企业信息'
    if status in (3,5):
        showbutton = True
    else:
        showbutton = False



    # 设置流程说明
    nodes = []
    nodes.append((0,request.user.date_joined,'企业填写企业信息　　下一步：上传企业财务报表'))
    cstatusall = CompanyStatus.objects.filter(companyInfo=cobj).order_by('id')
    rreasons = RejectReason.objects.filter(companyInfo=cobj)
    rreasonlst = []
    for reason in rreasons:
        text = reason.text
        rreasonlst.append([text[:39]])
        text = text[39:]
        while len(text) > 0:
            rreasonlst[-1].append(text[:39])
            text = text[39:]


    for cstatus in cstatusall:
        status = cstatus.status
        create_date = cstatus.create_date
        if status == 1:
            nodes.append((status,create_date,'企业上传财务报表　　下一步：企业进行自主评价'))
        elif status == 2:
            nodes.append((status,create_date,'企业进行自主评价　　下一步：企业提交信息'))
        elif status == 3:
            nodes.append((status,create_date,'企业提交信息　　下一步：所属孵化器审核企业信息'))
        elif status == 4:
            nodes.append((status,create_date,'所属孵化器审核企业信息'))
        elif status == 5:
            nodes.append(rreasonlst)
            nodes.append((status,create_date,'所属孵化器驳回企业信息　　下一步：企业提交信息'))
        elif status == 7:
            nodes.append((status,create_date,'所属孵化器修正企业评价　　孵化器进度已完成　　下一步：平台发送评估报告到机构'))
        elif status == 8:
            nodes.append((status,create_date,'平台发送评估报告到机构　　平台进度已完成　　下一步：等待机构反馈给平台'))
        elif status == 9:
            nodes.append((status,create_date,'投资机构反馈给平台　　投资机构进度已完成　　下一步：等待平台发送反馈信息'))
        elif status == 10:
            nodes.append((status,create_date,'您已收到来自平台的反馈信息'))
                

    res = render(request,'company_status.html',{'nodes':reversed(nodes),'showbutton':showbutton,
                'status_pic':status_pic,'status_text':status_text,'status_line':status_line})








    return res

# 企业确认提交信息
def confirm_view(request):

    cobj = CompanyInfo.objects.get(user=request.user)
    if cobj.status == 3 or cobj.status == 5:          
        cobj.status = 4
        cobj.save()
        CompanyStatus.objects.create(companyInfo=cobj,status=4)

    RejectReason.objects.filter(companyInfo=cobj,is_alive=True).update(is_alive=False)

    ren = redirect ('/admin/company/company_status/')
    return ren

# 孵化器驳回信息
def reject_view(request):
    _id = request.GET['id']
    reason = request.GET['reason']

    cobj = CompanyInfo.objects.get(id=_id)
    if cobj.status == 4:          
        cobj.status = 5
        cobj.save()
        if not CompanyStatus.objects.filter(companyInfo=cobj,status=5):
            CompanyStatus.objects.create(companyInfo=cobj,status=5)

    RejectReason.objects.create(companyInfo=cobj,text=reason)

    ren = redirect ('/admin/company/companyinfo/')
    return ren
    
# 孵化器审核 企业通过申请
def verify_view(request):
    _id = request.GET['id']
    cobj = CompanyInfo.objects.get(id=_id)

    if cobj.incubator.user == request.user:
        cobj.user.is_staff = True
        cobj.user.save()
    ren = redirect ('/admin/company/companyinfo/')
    return ren
    
def deldata_view(request):
    year = request.GET['year']
    model = request.GET['model']
    if model == 'cash_flow':
        M = CashFlow
    elif model == 'balance':
        M = Balance
    elif model == 'profit':
        M = Profit

    M.objects.filter(companyInfo__user=request.user,year=year).delete()
    ren = redirect ('/admin/company/'+model)
    return ren


def companyinfo_view(request):
    #  render
    group_name = None

    if not request.user.is_superuser:
        group_name = request.user.groups.all()[0].name
    if group_name == '企业用户':
        _id = CompanyInfo.objects.get(user=request.user).id
        ren = redirect ('/admin/company/companyinfo/%s'%_id)
        return ren
    # ren = redirect ('/admin/company/companyinfo/')
    ren = CompanyInfoAdmin(CompanyInfo,admin.AdminSite()).changelist_view(request)
    return ren

def financialsituation_view(request):
    _id = FinancialSituation.objects.get(companyInfo=CompanyInfo.objects.get(user=request.user)).id
    return HttpResponseRedirect('/admin/company/financialsituation/%s'%_id)
    
def productsandmarket_view(request):
    _id = ProductsAndMarket.objects.get(companyInfo=CompanyInfo.objects.get(user=request.user)).id
    return HttpResponseRedirect('/admin/company/productsandmarket/%s'%_id)

def technologyrd_view(request):
    _id = TechnologyRD.objects.get(companyInfo=CompanyInfo.objects.get(user=request.user)).id
    return HttpResponseRedirect('/admin/company/technologyrd/%s'%_id)

def serverrequest_view(request):
    _id = ServerRequest.objects.get(companyInfo=CompanyInfo.objects.get(user=request.user)).id
    return HttpResponseRedirect('/admin/company/serverrequest/%s'%_id)

def balance_add_view(request):
    return HttpResponseRedirect('/admin/company/balance/n/change/')

def balance_view(request,id_):
    if id_ == 'n':
        year = None
    else:
        year = Balance.objects.get(id=id_).year

    # year = request.GET.get('year')

    # yearlist = Balance.objects.filter(companyInfo=CompanyInfo.objects.get(user=request.user)).values('year').annotate(yearNum=Count("year"))
    # years = set()
    # for yea in yearlist:
    #     years.add(yea['year'])
    # years = sorted(years,key=lambda x: int(x))


    # if not year and years:
    #     year = max(years)

    

    bal_data = Balance.objects.all().filter(companyInfo=CompanyInfo.objects.get(user=request.user),year=year)
    bal_dict = { da.name:  da.value if da.value != 0 else '' for da in bal_data}

    data = []

    datab = [   ('b%s'%i ,s.strip('\n'))      for i,s in enumerate(B.split('\n'),4)   ]
    dataf = [   ('f%s'%i ,s.strip('\n'))      for i,s in enumerate(F.split('\n'),4)   ]

    
    datad = []
    datae = []
    for i in range(5,39):
        if i not in (5,17,18,26,28,37,38):
            datad.append(('d%s'%i,True,bal_dict.get('d%s'%i,'')))
            datae.append(('e%s'%i,True,bal_dict.get('e%s'%i,'')))
        else:
            datad.append(('d%s'%i,False))
            datae.append(('e%s'%i,False))

    datah = []
    datai = []
    for i in range(5,39):
        if i not in (5,18,19,27,28,29,35,36,37,38):
            datah.append(('h%s'%i,True,bal_dict.get('h%s'%i,'')))
            datai.append(('i%s'%i,True,bal_dict.get('i%s'%i,'')))
        else:
            datah.append(('h%s'%i,False))
            datai.append(('i%s'%i,False))


    data = zip(datab,datad,datae,dataf,datah,datai)

    cobj = CompanyInfo.objects.get(user=request.user)
    status = cobj.status
    if status == 5 or status < 4:
        status = True
    else:
        status = False

    return render(request,'balance.html',{'data':data,'status':status,'year':year})


def balance_submit_table_view(request):



    year = request.POST['year']
    for x in request.POST:
        if x == 'year':
            pass
        elif len(x)<6:
            if not request.POST[x]:
                res = 0
            else:
                res = request.POST[x]

            try:
                try:
                    bal = Balance.objects.get(companyInfo=CompanyInfo.objects.get(user=request.user),year=year,name=x)
                    bal.value=res
                    bal.save()
                except Balance.DoesNotExist as e:
                    Balance(companyInfo=CompanyInfo.objects.get(user=request.user),year=year,
                            name=x,value=res).save()
            except ValueError as e:
                pass




    cobj = CompanyInfo.objects.get(user=request.user)
    if cobj.status == 1:          
        if Balance.objects.filter(companyInfo=cobj) and Profit.objects.filter(companyInfo=cobj) and\
            CashFlow.objects.filter(companyInfo=cobj):
                cobj.status = 2
                cobj.save()
                if not CompanyStatus.objects.filter(companyInfo=cobj,status=2):
                    CompanyStatus.objects.create(companyInfo=cobj,status=2)

    messages.success(request, '数据提交成功')

    ren = redirect ('/admin/company/balance/')
    return ren

# def profit_view(request):
#     year = 2018
#     bal_data = Profit.objects.all().filter(companyInfo=CompanyInfo.objects.get(user=request.user),year=year)
#     bal_dict = { da.name:da.value for da in bal_data}

#     dataa = [   ('a%s'%i ,s.strip('\n'))      for i,s in enumerate(profit_str.split('\n'),5)   ]
#     datac = []
#     for i in range(5,31):
#         if i not in (5,6,9,10,23,28,30):
#             datac.append(('c%s'%i,True,bal_dict.get('c%s'%i,'')))
#         else:
#             datac.append(('c%s'%i,False))

#     data = zip(dataa,datac)



#     return render(request,'profit.html',{'data':data})




# def profit_submit_table_view(request):
#     year = 2018
#     # data = { x:request.POST[x]    for x in request.POST if len(x)<6 and request.POST[x]}
#     for x in request.POST:
#         if len(x)<6 and request.POST[x]:
#             try:
#                 bal = Profit.objects.get(companyInfo=CompanyInfo.objects.get(user=request.user),year=year,name=x)
#                 bal.value=request.POST[x]
#                 bal.save()
#             except Profit.DoesNotExist as e:
#                 Profit(companyInfo=CompanyInfo.objects.get(user=request.user),year=year,
#                         name=x,value=request.POST[x]).save()

#     ren = redirect ('/admin/company/profit/')
#     return ren




def profit_add_view(request):
    return HttpResponseRedirect('/admin/company/profit/n/change/')



def profit_view(request,id_):
    
    # year = request.GET.get('year')
    # yearlist = Profit.objects.filter(companyInfo=CompanyInfo.objects.get(user=request.user)).values('year').annotate(yearNum=Count("year"))
    # years = set()
    # for yea in yearlist:
    #     years.add(yea['year'])
    # years = sorted(years,key=lambda x: int(x))
    # if not year and years:
    #     year = max(years)
    if id_ == 'n':
        year = None
    else:
        year = Profit.objects.get(id=id_).year

    bal_data = Profit.objects.all().filter(companyInfo=CompanyInfo.objects.get(user=request.user),year=year)
    bal_dict = { da.name:da.value for da in bal_data}

    dataa = [   ('a%s'%i ,s.strip('\n'))      for i,s in enumerate(profit_str.split('\n'),5)   ]
    datac = []
    for i in range(5,32):
        if i not in (5,6,9,10,24,29,31):
            datac.append(('c%s'%i,True,bal_dict.get('c%s'%i,'')))
        else:
            datac.append(('c%s'%i,False))
    datad = []
    for i in range(5,31):
        if i not in (5,6,9,10,24,29,31):
            datad.append(('d%s'%i,True,bal_dict.get('d%s'%i,'')))
        else:
            datad.append(('d%s'%i,False))

    data = zip(dataa,datac,datad)

    cobj = CompanyInfo.objects.get(user=request.user)
    status = cobj.status
    if status == 5 or status < 4:
        status = True
    else:
        status = False


    return render(request,'profit.html',{'data':data,'status':status,'year':year})




def profit_submit_table_view(request):
    year = request.POST['year']
    # data = { x:request.POST[x]    for x in request.POST if len(x)<6 and request.POST[x]}
    for x in request.POST:
        if len(x)<6 and request.POST[x]:
            try:
                try:
                    bal = Profit.objects.get(companyInfo=CompanyInfo.objects.get(user=request.user),year=year,name=x)
                    bal.value=request.POST[x]
                    bal.save()
                except Profit.DoesNotExist as e:
                    Profit(companyInfo=CompanyInfo.objects.get(user=request.user),year=year,
                            name=x,value=request.POST[x]).save()
            except ValueError as e:
                pass

    cobj = CompanyInfo.objects.get(user=request.user)
    # print(cobj.status)
    # print(Balance.objects.filter(companyInfo=cobj).count())
    # print(Profit.objects.filter(companyInfo=cobj).count())
    # print(CashFlow.objects.filter(companyInfo=cobj).count())
    if cobj.status == 1:          
        if Balance.objects.filter(companyInfo=cobj) and Profit.objects.filter(companyInfo=cobj) and\
            CashFlow.objects.filter(companyInfo=cobj):
                cobj.status = 2
                cobj.save()
                if not CompanyStatus.objects.filter(companyInfo=cobj,status=2):
                    CompanyStatus.objects.create(companyInfo=cobj,status=2)

    messages.success(request, '数据提交成功')
    ren = redirect ('/admin/company/profit/')
    return ren


def cash_flow_add_view(request):
    return HttpResponseRedirect('/admin/company/cashflow/n/change/')



def cash_flow_view(request,id_):
    getdatadict = {}
    def get_other_data(name):
        def get_data(M,name):
            if M == Profit:
                tname = 'p'+name
            elif M == Balance:
                tname = 'b'+name
            try:
                da = getdatadict.get(tname)
                if not da:
                    da = M.objects.get(companyInfo=CompanyInfo.objects.get(user=request.user),year=year,name=name).value
                    getdatadict[tname] = da
                return da
            except (Profit.DoesNotExist,Balance.DoesNotExist) as e:
                getdatadict[tname] = 0
                return 0

        if name == 'd6':
            pc7 = get_data(Profit,'c7')
            pc8 = get_data(Profit,'c8')
            pc6 = pc7 + pc8
            bd9 = get_data(Balance,'d9')
            be9 = get_data(Balance,'e9')
            bd8 = get_data(Balance,'d8')
            be8 = get_data(Balance,'e8')
            bi10 = get_data(Balance,'i10')
            bh10 = get_data(Balance,'h10')
            print('d6表外数据录入怎么处理')
            resda = pc6*1.17+(bd9-be9)+(bd8-be8)+(bi10-bh10) #- other
        elif name == 'd10':
            pc11 = get_data(Profit,'c11')
            pc12 = get_data(Profit,'c12')
            pc10 = pc11 + pc12
            be10 = get_data(Balance,'e10')
            bd10 = get_data(Balance,'d10')
            bh7 = get_data(Balance,'h7')
            bi7 = get_data(Balance,'i7')
            bh8 = get_data(Balance,'h8')
            bi8 = get_data(Balance,'i8')
            resda = (pc10+be10-bd10)*1.17 + (bh7-bi7) + (bh8-bi8)
        elif name == 'd17':
            bd21 = get_data(Balance,'d21')
            be21 = get_data(Balance,'e21')
            resda = bd21-be21 if be21-bd21 < 0 else 0
        elif name == 'd22':
            bd24 = get_data(Balance,'d24')
            be24 = get_data(Balance,'e24')
            resda = be24-bd24
        elif name == 'd23':
            bd21 = get_data(Balance,'d21')
            be21 = get_data(Balance,'e21')
            resda = be21-bd21 if be21-bd21 > 0 else 0 
        elif name == 'd28':
            bi30 = get_data(Balance,'i30')
            bh30 = get_data(Balance,'h30')
            resda = bi30-bh30

        elif name == 'd29':
            print('没有 bi5和bh5')
            bi5 = get_data(Balance,'i5')
            bh5 = get_data(Balance,'h5')
            bi19 = get_data(Balance,'i19')
            bh19 = get_data(Balance,'h19')
            resda = (bi5-bh5)+(bi19-bh19)

        elif name == 'g6':
            c7 = get_data(Profit,'c7')
            c8 = get_data(Profit,'c8')
            c11 = get_data(Profit,'c11')
            c12 = get_data(Profit,'c12')
            c13 = get_data(Profit,'c13')
            c14 = get_data(Profit,'c14')
            c15 = get_data(Profit,'c15')
            c17 = get_data(Profit,'c17')
            c19 = get_data(Profit,'c19')
            c20 = get_data(Profit,'c20')
            c21 = get_data(Profit,'c21')
            c24 = get_data(Profit,'c24')
            c26 = get_data(Profit,'c26')
            c29 = get_data(Profit,'c29')
            pc30 = c7+c8-c11-c12-c13-c14-c15-c17-c19-c20-c21+c24-c26-c29
            resda = pc30

        elif name == 'g8':
            be25 = get_data(Balance,'e25')
            bd25 = get_data(Balance,'d25')
            resda = be25-bd25

        elif name == 'g11':
            bd15 = get_data(Balance,'d15')
            be15 = get_data(Balance,'e15')
            resda = bd15-be15

        elif name == 'g12':
            bi16 = get_data(Balance,'i16')
            bh16 = get_data(Balance,'h16')
            resda = bi16-bh16

        elif name == 'g16':
            pc21 = get_data(Profit,'c21')
            resda = -pc21

        elif name == 'g18':
            bd14 = get_data(Balance,'d14')
            be14 = get_data(Balance,'e14')
            resda = bd14-be14

        elif name == 'g19':
            bd9 = get_data(Balance,'d9')
            be9 = get_data(Balance,'e9')
            bd10 = get_data(Balance,'d10')
            be10 = get_data(Balance,'e10')
            bd13 = get_data(Balance,'d13')
            be13 = get_data(Balance,'e13')

            resda = bd9-be9+bd10-be10+bd13-be13

        elif name == 'g20':
            h6 = get_data(Balance,'h6')
            h7 = get_data(Balance,'h7')
            h8 = get_data(Balance,'h8')
            h9 = get_data(Balance,'h9')
            h10 = get_data(Balance,'h10')
            h11 = get_data(Balance,'h11')
            h12 = get_data(Balance,'h12')
            h13 = get_data(Balance,'h13')
            h14 = get_data(Balance,'h14')
            h15 = get_data(Balance,'h15')
            h16 = get_data(Balance,'h16')
            h17 = get_data(Balance,'h17')
            h18 = get_data(Balance,'h18')


            i6 = get_data(Balance,'i6')
            i7 = get_data(Balance,'i7')
            i8 = get_data(Balance,'i8')
            i9 = get_data(Balance,'i9')
            i10 = get_data(Balance,'i10')
            i11 = get_data(Balance,'i11')
            i12 = get_data(Balance,'i12')
            i13 = get_data(Balance,'i13')
            i14 = get_data(Balance,'i14')
            i15 = get_data(Balance,'i15')
            i16 = get_data(Balance,'i16')
            i17 = get_data(Balance,'i17')
            i18 = get_data(Balance,'i18')
            bh18 = h6+h7+h8+h9+h10+h11+h12+h13+h14+h15+h16+h17+h18
            bi18 = i6+i7+i8+i9+i10+i11+i12+i13+i14+i15+i16+i17+h18
            resda = bi18-bh18

        elif name == 'g34':
            be6 = get_data(Balance,'e6')
            resda = be6

        elif name == 'g35':
            bd6 = get_data(Balance,'d6')
            resda = bd6
        if resda:
            return round(resda,2)
        return resda



    # year = request.GET.get('year')

    # yearlist = CashFlow.objects.filter(companyInfo=CompanyInfo.objects.get(user=request.user)).values('year').annotate(yearNum=Count("year"))
    # years = set()
    # for yea in yearlist:
    #     years.add(yea['year'])
    # years = sorted(years,key=lambda x: int(x))
    # if not year and years:
    #     year = max(years)

    if id_ == 'n':
        year = None
    else:
        year = CashFlow.objects.get(id=id_).year

    if year:
        bal_data = CashFlow.objects.filter(companyInfo=CompanyInfo.objects.get(user=request.user),year=year)
        bal_dict = { da.name:da.value for da in bal_data}
    else:
        bal_dict = {}

    datab = [   ('b%s'%i ,s.strip('\n'))      for i,s in enumerate(cash_flow_strb.split('\n'),5)   ]
    datae = [   ('e%s'%i ,s.strip('\n'))      for i,s in enumerate(cash_flow_stre.split('\n'),5)   ]
    datad = []
    datag = []


    for i in range(5,39):
        if i in (7,18,19,20,24,30,33,34,      8,11,12,13,45,55):
            datad.append(('d%s'%i,True,bal_dict.get('d%s'%i,'')))
        elif i in (6,17,22,23,28,29):
            datad.append(('d%s'%i,get_other_data('d%s'%i)))
        else:
            datad.append(('d%s'%i,False))


    for i in range(5,39):
        if i in (7,9,13,14,      10,15,17,27,28,29,36,37):
            datag.append(('g%s'%i,True,bal_dict.get('g%s'%i,'')))
        elif i in (6,8,11,12,16,18,19,20,34,35):
            datag.append(('g%s'%i,get_other_data('g%s'%i)))
        else:
            datag.append(('g%s'%i,False))
    # print('----------changdu----------')
    # print(len(datab),len(datad),len(datae),len(datag))
    data = zip(datab,datad,datae,datag)



    cobj = CompanyInfo.objects.get(user=request.user)
    status = cobj.status
    if status == 5 or status < 4:
        status = True
    else:
        status = False
    # print(year)
    return render(request,'cash_flow.html',{'data':data,'status':status,'year':year})

    




def cash_flow_submit_table_view(request):
    # data = { x:request.POST[x]    for x in request.POST if len(x)<6 and request.POST[x]}
    year = request.POST['year']
    for x in request.POST:
        if x == 'year':
            pass
        elif len(x)<6 and request.POST[x]:
            try:
                try:
                    bal = CashFlow.objects.get(companyInfo=CompanyInfo.objects.get(user=request.user),year=year,name=x)
                    bal.value=request.POST[x]
                    bal.save()
                except CashFlow.DoesNotExist as e:
                    CashFlow(companyInfo=CompanyInfo.objects.get(user=request.user),year=year,
                            name=x,value=request.POST[x]).save()
            except ValueError as e:
                pass


    cobj = CompanyInfo.objects.get(user=request.user)
    if cobj.status == 1:          
        if Balance.objects.filter(companyInfo=cobj) and Profit.objects.filter(companyInfo=cobj) and\
            CashFlow.objects.filter(companyInfo=cobj):
                cobj.status = 2
                cobj.save()
                if not CompanyStatus.objects.filter(companyInfo=cobj,status=2):
                    CompanyStatus.objects.create(companyInfo=cobj,status=2)

    messages.success(request, '数据提交成功')
    ren = redirect ('/admin/company/cashflow/')
    return ren

def independentevaluationofenterprises_view(request,arg1):
    group_name = None
    if request.user.is_superuser:
        return IndependentEvaluationOfEnterprisesAdmin(IndependentEvaluationOfEnterprises,admin.AdminSite()).change_view(request,arg1)
        group_name = None
    else:
        group_name = request.user.groups.all()[0].name

    if group_name == '企业用户':
        return IndependentEvaluationOfEnterprisesAdmin(IndependentEvaluationOfEnterprises,admin.AdminSite()).change_view(request,arg1)
    elif group_name == '孵化器用户':
        iobj = IndependentEvaluationOfEnterprises.objects.get(id=arg1)
        try:
            eobj = EvaluationOfEnterprises.objects.get(companyInfo=iobj.companyInfo)
        except EvaluationOfEnterprises.DoesNotExist as e:
            eobj = EvaluationOfEnterprises.objects.create(companyInfo=iobj.companyInfo)
        data = {'isocre1':iobj.external_environment,
                'isocre2':iobj.products_and_market,
                'isocre3':iobj.technology_R_D,
                'isocre4':iobj.team,
                }
        return EvaluationOfEnterprisesAdmin(EvaluationOfEnterprises,admin.AdminSite()).change_view(request,str(eobj.id),extra_context=data)

        

def evaluationofenterprises_to_independentevaluationofenterprises_view(request):
    return redirect ('/admin/company/independentevaluationofenterprises/')









# class ConfigView(generic.TemplateView):
#     template_name = 'admin/company/independentevaluationofenterprises/change_form.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         print(kwargs)
#         print(context)
#         return context



# 4-38
B = '''流动资产：
货币资金
交易性金融资产
应收票据
应收账款
预付账款
应收利息
应收股利
其他应收款
存货
一年内到期的非流动资产
其他流动资产
流动资产合计
非流动资产：
可供出售金融资产
持有至到期投资
长期应收款
长期股权投资
投资性房地产
固定资产原价
　减:累计折旧
固定资产净值
　减:固定资产减值准备
固定资产净额
在建工程
工程物资
固定资产清理
无形资产
开发支出
长期待摊费用
递延所得税资产
其他非流动资产
非流动资产合计
资产总计'''

F='''流动负债：
短期借款
交易性金融负债
应付票据
应付账款
预收账款
应付职工薪酬
应交税费
应付利息
应付股利
其他应付款
一年内到期的非流动负债
其他流动负债
流动负债合计
非流动负债：
长期借款
应付债券
长期应付款
专项应付款
预计负债
递延所得税负债
其他非流动负债
非流动负债合计
负债合计
所有者权益
实收资本（或股本）
资本公积
减：库存股
盈余公积
未分配利润
所有者权益合计


负债及所有者权益合计'''



profit_str='''一、营业总收入
营业收入
　其中：主营业务收入
　　　　其他业务收入
二、营业总成本
营业成本
　其中：主营业务成本
　　　　其他业务成本
　　　　营业税金及附加
　　　　销售费用
　　　　管理费用
　　　　　其中：研发费用
　　　　财务费用
　　　　　其中：利息费用
　　　　　利息收入
　　　　资产减值损失
　　加：公允价值变动收益（损失以“－”号填列）
　　　　投资收益（损失以“－”号填列）
　　　　　其中:对联营企业和合营企业的投资收益
三、营业利润（亏损以“－”号填列）
　　加：营业外收入
　　　　　其中：补贴收入
　　减：营业外支出
　　　　　其中：非流动资产处置损失
四、利润总额（亏损总额以“－”号填列）
　　减：所得税费用
五、净利润（净亏损以“－”号填列）'''





cash_flow_strb='''一、经营活动产生的现金流量：
　　　　销售商品、提供劳务收到的现金
　　　　收到的税费返还
　　　　收到的其他与经营活动有关的现金
现金流入小计
　　　　购买商品、接受劳务支付的现金
　　　　支付给职工以及为职工支付的现金
　　　　支付的各项税费
　　　　支付的其他与经营活动有关的现金
现金流出小计
　　　　经营活动产生的现金流量净额
二、投资活动产生的现金流量：
　　　　收回投资所收到的现金
　　　　取得投资收益所收到的现金
　　　　处置固定资产、无形资产和其他长期资产所收回的现金净额
　　　　收到的其他与投资活动有关的现金
现金流入小计
　　　　购建固定资产、无形资产和其他长期资产所支付的现金
　　　　投资所支付的现金
　　　　支付的其他与投资活动有关的现金
现金流出小计
　　　投资活动产生的现金流量净额
三、筹资活动产生的现金流量：
　　　　吸收投资所收到的现金
　　　　借款所收到的现金
　　　　收到的其他与筹资活动有关的现金
现金流入小计
　　　　偿还债务所支付的现金
　　　　分配股利、利润或偿付利息所支付的现金
　　　　支付的其他与筹资活动有关的现金
现金流出小计
　　　　筹资活动产生的现金流量净额
四、汇率变动对现金的影响
五、现金及现金等价物净增加额'''



cash_flow_stre='''1、将净利润调节为经营活动现金流量：
　　净利润
　　加：计提的资产减值准备
　　　　固定资产折旧
　　　　无形资产摊销
　　　　长期待摊费用摊销
　　　　待摊费用减少（减：增加）
　　　　预提费用增加（减：减少）
　　　　处置固定资产、无形资产和其他长期资产的损失（减：收益）
　　　　固定资产报废损失
　　　　财务费用
　　　　投资损失（减：收益）
　　　　递延税款贷项（减：借项）
　　　　存货的减少（减：增加）
　　　　经营性应收项目的减少（减：增加）
　　　　经营性应付项目的增加（减：减少）
　　　　其他
　　经营活动产生的现金流量净额



2、不涉及现金收支的投资和筹资活动：
　　债务转为资本
　　一年内到期的可转换公司债券
　　融资租入固定资产



3、现金及现金等价物净增加情况：
　　现金的期末余额
　　减：现金的期初余额
　　加：现金等价物的期末余额
　　减：现金等价物的期初余额
　　现金及现金等价物净增加额'''