from django.shortcuts import render,redirect

# Create your views here.
from django.contrib import auth
from django.contrib.auth.models import User,Group
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from company.models import *
from incubator.models import Incubator
from institution.models import Institution
from pprint import pprint
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
# 用户注册
# 
# 
# 
# 

def my_register(request):
    errors = []
    if request.method == 'POST':

        # name
        # credit_code
        # phone
        # business_license_pic
        
        

        if request.POST['password'] != request.POST['password2']:
            errors.append('两次输入密码不一致')
        # print(len(User.objects.all().filter(username = request.POST['username'])))
        if len(User.objects.all().filter(username = request.POST['username'])) == 1:
            errors.append('用户名已被使用')

        if errors:
            return render(request,'res.html',{'errors':errors})


        account = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(account,'xx@qq.com',password)
        user.save()
        userlogin = auth.authenticate(username = account,password = password)
        auth.login(request,userlogin)

        if request.POST['type'] == '1':
            image = request.FILES['business_license_pic']

            # set user
            user.is_active = True
            user.is_staff = True
            user.groups.add(Group.objects.get(name='企业用户'))
            user.save()

            # set company
            need_data = ['name','credit_code','phone','incubator']
            dic = {  da:request.POST[da]    for da in request.POST if da in need_data}
            dic['incubator'] = Incubator.objects.get(name=dic['incubator'])
            com = CompanyInfo.objects.create(user=user,business_license_pic=image,**dic)
            FinancialSituation.objects.create(companyInfo=com)
            ProductsAndMarket.objects.create(companyInfo=com)
            TechnologyRD.objects.create(companyInfo=com)
            ServerRequest.objects.create(companyInfo=com)
            return HttpResponseRedirect('/admin')

        elif request.POST['type'] == '2':

            user.is_active = True
            user.is_staff = True
            user.groups.add(Group.objects.get(name='孵化器用户'))
            user.save()
            need_data = ['name','phone']
            dic = {  da:request.POST[da]    for da in request.POST if da in need_data}
            inc = Incubator.objects.create(user=user,**dic)
            return HttpResponseRedirect('/admin')

        elif request.POST['type'] == '3':

            user.is_active = True
            user.is_staff = True
            user.groups.add(Group.objects.get(name='机构用户'))
            user.save()
            need_data = ['name','phone']
            dic = {  da:request.POST[da]    for da in request.POST if da in need_data}
            inc = Institution.objects.create(user=user,type=1,**dic)
            return HttpResponseRedirect('/admin')

        elif request.POST['type'] == '4':

            user.is_active = True
            user.is_staff = True
            user.groups.add(Group.objects.get(name='机构用户'))
            user.save()
            need_data = ['name','phone']
            dic = {  da:request.POST[da]    for da in request.POST if da in need_data}
            inc = Institution.objects.create(user=user,type=2,**dic)
            return HttpResponseRedirect('/admin')
        
    incubators = Incubator.objects.all()
    return render(request,'res.html',{'errors':errors,'incubators':incubators})


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

    incubators = Incubator.objects.all()
    print(incubators)
    print(len(incubators))
    return render(request,'register.html', {'errors': errors,'incubators':incubators})

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

def inital_company_data(user):
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
    print(1111111111)
    errors =[]
    username = None
    password = None
    if request.method == "POST":
        if not request.POST.get('username'):
            errors.append('用户名不能为空')
        else:
            username = request.POST.get('username')

        if not request.POST.get('password'):
            errors = request.POST.get('密码不能为空')
        else:
            password = request.POST.get('password')

        if username is not None and password is not None:
            user = auth.authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    auth.login(request,user)
                    return HttpResponseRedirect('/admin')
                else:
                    errors.append('用户未激活')
            else:
                errors.append('用户名或密码错误')
    return render(request,'login.html', {'errors': errors})

# 用户退出
def my_logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/blog')



