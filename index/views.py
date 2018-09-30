from django.shortcuts import render,redirect

# Create your views here.
from django.contrib import auth
from django.contrib.auth.models import User,Group
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from .models import *
from pprint import pprint
# 用户注册
# 
# 


def companyinfo_view(request):
    #  render
    
    _id = CompanyInfo.objects.get(user=request.user).id
    ren = redirect ('/admin/index/companyinfo/%s'%_id)
    return ren
    
def financialsituation_view(request):
    _id = FinancialSituation.objects.get(companyInfo=CompanyInfo.objects.get(user=request.user)).id
    return HttpResponseRedirect('/admin/index/financialsituation/%s'%_id)
    
def productsandmarket_view(request):
    _id = ProductsAndMarket.objects.get(companyInfo=CompanyInfo.objects.get(user=request.user)).id
    return HttpResponseRedirect('/admin/index/productsandmarket/%s'%_id)

def technologyrd_view(request):
    _id = TechnologyRD.objects.get(companyInfo=CompanyInfo.objects.get(user=request.user)).id
    return HttpResponseRedirect('/admin/index/technologyrd/%s'%_id)

def serverrequest_view(request):
    _id = ServerRequest.objects.get(companyInfo=CompanyInfo.objects.get(user=request.user)).id
    return HttpResponseRedirect('/admin/index/serverrequest/%s'%_id)

def balance_view(request):


    data = []

    datab = [   ('b%s'%i ,s.strip())      for i,s in enumerate(B.split('\n'),4)   ]
    dataf = [   ('f%s'%i ,s.strip())      for i,s in enumerate(F.split('\n'),4)   ]

    
    datad = []
    datae = []
    for i in range(5,39):
        if i not in (5,17,18,26,28,37,38):
            datad.append(('d%s'%i,True))
            datae.append(('e%s'%i,True))
        else:
            datad.append(('d%s'%i,False))
            datae.append(('e%s'%i,False))

    datah = []
    datai = []
    for i in range(5,39):
        if i not in (5,18,19,27,28,29,35,36,37,38):
            datah.append(('h%s'%i,True))
            datai.append(('i%s'%i,True))
        else:
            datah.append(('h%s'%i,False))
            datai.append(('i%s'%i,False))


    data = zip(datab,datad,datae,dataf,datah,datai)
    return render(request,'balance.html',{'data':data})












@csrf_exempt
def register(request):
    errors = []
    account = None
    password = None
    password2 = None
    email = None
    CompareFlag = False

    # pprint(User.objects.get(id=5).groups)
    if request.method == 'POST':
        if not request.POST.get('account'):
            errors.append('用户名不能为空')
        else:
            account = request.POST.get('account')

        if not request.POST.get('password'):
            errors.append('密码不能为空')
        else:
            password = request.POST.get('password')
        if not request.POST.get('password2'):
            errors.append('确认密码不能为空')
        else:
            password2 = request.POST.get('password2')

        # if not request.POST.get('email'):
        #     errors.append('邮箱不能为空')
        # else:
        #     email = request.POST.get('email')

        if password is not None:
            if password == password2:
                CompareFlag = True
            else:
                errors.append('两次输入密码不一致')

        if account is not None and password is not None and password2 is not None and CompareFlag :
            user = User.objects.create_user(account,'11@qq.com',password)
            user.save()

            userlogin = auth.authenticate(username = account,password = password)
            auth.login(request,userlogin)
            inital_data(user)
            return HttpResponseRedirect('/admin')

    return render(request,'register.html', {'errors': errors})

def inital_data(user):
    user.is_active = True
    user.is_staff = True
    user.groups.add(Group.objects.get(name='企业用户'))
    user.save()

    
    com = CompanyInfo.objects.create(user=user,name='请填写企业名称')
    FinancialSituation.objects.create(companyInfo=com)
    ProductsAndMarket.objects.create(companyInfo=com)
    TechnologyRD.objects.create(companyInfo=com)
    ServerRequest.objects.create(companyInfo=com)

# 用户登录
@csrf_exempt
def my_login(request):
    errors =[]
    account = None
    password = None
    if request.method == "POST":
        if not request.POST.get('account'):
            errors.append('用户名不能为空')
        else:
            account = request.POST.get('account')

        if not request.POST.get('password'):
            errors = request.POST.get('密码不能为空')
        else:
            password = request.POST.get('password')

        if account is not None and password is not None:
            user = auth.authenticate(username=account,password=password)
            if user is not None:
                if user.is_active:
                    auth.login(request,user)
                    return HttpResponseRedirect('/blog')
                else:
                    errors.append('用户名错误')
            else:
                errors.append('用户名或密码错误')
    return render(request,'login.html', {'errors': errors})

# 用户退出
def my_logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/blog')




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