from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
# Create your views here.
from django.contrib import auth
from django.contrib.auth.models import User,Group
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from .models import *
from pprint import pprint
from django.db.models import F
from django.contrib import admin
from .admin import IndependentEvaluationOfEnterprisesAdmin,EvaluationOfEnterprisesAdmin
# 用户注册
# 
# 


def companyinfo_view(request):
    #  render
    group_name = None
    if not request.user.is_superuser:
        group_name = request.user.groups.all()[0].name
    if group_name == '企业用户':
        _id = CompanyInfo.objects.get(user=request.user).id
        ren = redirect ('/admin/company/companyinfo/%s'%_id)
        return ren
    ren = redirect ('/admin/company/companyinfo/')
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

def balance_view(request):

    year = 2018
    bal_data = Balance.objects.all().filter(companyInfo=CompanyInfo.objects.get(user=request.user),year=year)
    bal_dict = { da.name:da.value for da in bal_data}

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
    return render(request,'balance.html',{'data':data})


def balance_submit_table_view(request):
    year = 2018
    # data = { x:request.POST[x]    for x in request.POST if len(x)<6 and request.POST[x]}
    for x in request.POST:
        if len(x)<6 and request.POST[x]:
            try:
                bal = Balance.objects.get(companyInfo=CompanyInfo.objects.get(user=request.user),year=year,name=x)
                bal.value=request.POST[x]
                bal.save()
            except Balance.DoesNotExist as e:
                Balance(companyInfo=CompanyInfo.objects.get(user=request.user),year=year,
                        name=x,value=request.POST[x]).save()

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

def profit_view(request):
    year = 2018
    bal_data = Profit.objects.all().filter(companyInfo=CompanyInfo.objects.get(user=request.user),year=year)
    bal_dict = { da.name:da.value for da in bal_data}

    dataa = [   ('a%s'%i ,s.strip('\n'))      for i,s in enumerate(profit_str.split('\n'),5)   ]
    datac = []
    for i in range(5,31):
        if i not in (5,6,9,10,23,28,30):
            datac.append(('c%s'%i,True,bal_dict.get('c%s'%i,'')))
        else:
            datac.append(('c%s'%i,False))

    data = zip(dataa,datac)



    return render(request,'profit.html',{'data':data})




def profit_submit_table_view(request):
    year = 2018
    # data = { x:request.POST[x]    for x in request.POST if len(x)<6 and request.POST[x]}
    for x in request.POST:
        if len(x)<6 and request.POST[x]:
            try:
                bal = Profit.objects.get(companyInfo=CompanyInfo.objects.get(user=request.user),year=year,name=x)
                bal.value=request.POST[x]
                bal.save()
            except Profit.DoesNotExist as e:
                Profit(companyInfo=CompanyInfo.objects.get(user=request.user),year=year,
                        name=x,value=request.POST[x]).save()

    ren = redirect ('/admin/company/profit/')
    return ren

def cash_flow_view(request):
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

    year = 2018
    bal_data = CashFlow.objects.all().filter(companyInfo=CompanyInfo.objects.get(user=request.user),year=year)
    bal_dict = { da.name:da.value for da in bal_data}

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
            datad.append(('g%s'%i,get_other_data('g%s'%i)))
        else:
            datag.append(('g%s'%i,False))
    data = zip(datab,datad,datae,datag)





    return render(request,'cash_flow.html',{'data':data})

    




def cash_flow_submit_table_view(request):
    year = 2018
    # data = { x:request.POST[x]    for x in request.POST if len(x)<6 and request.POST[x]}
    for x in request.POST:
        if len(x)<6 and request.POST[x]:
            try:
                bal = CashFlow.objects.get(companyInfo=CompanyInfo.objects.get(user=request.user),year=year,name=x)
                bal.value=request.POST[x]
                bal.save()
            except CashFlow.DoesNotExist as e:
                CashFlow(companyInfo=CompanyInfo.objects.get(user=request.user),year=year,
                        name=x,value=request.POST[x]).save()

    ren = redirect ('/admin/company/cash_flow/')
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
        print(eobj.id)
        return EvaluationOfEnterprisesAdmin(EvaluationOfEnterprises,admin.AdminSite()).change_view(request,str(eobj.id))





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
　　　　　其中：利息收入
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
　　现金及现金等价物净增加额
'''