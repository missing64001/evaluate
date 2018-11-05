from django.shortcuts import render,redirect

# Create your views here.
from django.contrib import auth,admin
from django.contrib.auth.models import User,Group,Permission
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from company.models import *
from incubator.models import Incubator
from institution.models import Institution
from pprint import pprint
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.views import generic
# from django.db.models import get_app_list
from pprint import pprint
from django.template.response import TemplateResponse
# class Index(generic.TemplateView):
#     template_name = 'admin/index.html'
#     def get_context_data(self, **kwargs):
#         pprint(kwargs)
#         context = super().get_context_data( **kwargs)
#         # print(context)
#         # context['app_list'] = admin.site.get_app_list(request)

#         # context['status_code'] = 200
#         # # print(context['app_list'])
#         # print(111111111)
#         return context




                # (0,'完成'),
                # (1,'填写企业信息'),
                # (2,'上传财务报表'),
                # (3,'企业自我评价'),
                # (4,'请确认提交'),

                # (5,'孵化器驳回信息'), #修改后确认提交
                # (6,'孵化器审核信息'),
                # (7,'孵化器修正评价'),

                # (8,'平台发送报告'),

                # (9,'机构反馈报告'),

                # (10,'用户获得反馈'),

def MyAdminIndex(request):
    self = admin.site

    app_list = self.get_app_list(request)

    # 孵化器驳回信息
    # 孵化器审核信息
    # 孵化器修正评价

    context = dict(
        self.each_context(request),
        title=self.index_title,
        app_list=app_list,
    )
    request.current_app = self.name

    if not request.user.is_authenticated():
        return HttpResponseRedirect('/admin/login')

    if get_user_group(request,'企业用户'):
        com = CompanyInfo.objects.get(status__gte = 0,user=request.user)
        status = com.status
        company_status_main_un = ['数据已提交','孵化器进度','平台进度','机构进度']
        company_status = [
        ['数据已提交','2',[['填写企业信息','2'],['上传财务报表','2'],['企业自我评价','2'],['数据已提交','2']]],
        ['孵化器修正评价','2',[]],
        ['平台发送报告','2'],
        ['机构反馈报告','2'],
        ['用户获得反馈','2'],
        ]

        if status < 10:
            company_status[4][1] = '1'

        if status < 9:
            company_status[3][1] = '1'
            company_status[4][1] = '4'

        if status < 8:
            company_status[2][1] = '1'
            company_status[3][1] = '4'
            company_status[3][0] = company_status_main_un[3]

        if status < 7:
            company_status[1][1] = '1'
            company_status[2][1] = '4'
            company_status[1][0] = '孵化器修正评价'
            company_status[2][0] = company_status_main_un[2]
            # company_status[1][0] = company_status_main_un[1]

        if status == 5:
            robjs = RejectReason.objects.filter(companyInfo=com,is_alive=True)
            robjs = [( te['text'],'3')      for te in robjs.values('text')]
            company_status[1][1] = '3'
            company_status[1][0] = '孵化器驳回信息'
            company_status[1][2] = robjs
            company_status[0][1] = '3'
            company_status[0][0] = '请再次确认提交'
            company_status[0][2] = []

        if status < 5:
            company_status[1][1] = '1'
            company_status[1][0] = '孵化器审核信息'

        if status < 4:
            company_status[1][1] = '4'
            company_status[1][0] = company_status_main_un[1]

        if status == 3:
            company_status[0][0] = '请确认提交数据'
            company_status[0][1] = '3'
            company_status[0][2] = []

        if status < 3:
            company_status[0][1] = '1'
            company_status[0][0] = '企业自我评价'
            company_status[0][2][3][1] = '4'
            company_status[0][2][2][1] = '1'

        if status < 2:
            company_status[0][0] = '上传财务报表'
            company_status[0][2][1][1] = '1'
            company_status[0][2][3][1] = '4'
            company_status[0][2][2][1] = '4'

        if status < 1:
            company_status[0][0] = '填写企业信息'
            company_status[0][2][0][1] = '1'
            company_status[0][2][1][1] = '4'


        context['company_status']=company_status

    # context.update(extra_context or {})

    

    return TemplateResponse(request, self.index_template or 'admin/index.html', context)









    return site.index(request)
# 用户注册
# 


def my_register(request):

    errors = []
    if request.method == 'POST':

        if request.POST['password'] != request.POST['password2']:
            errors.append('两次输入密码不一致')

        if len(request.POST['password2']) < 6:
            errors.append('密码小于六位')
        # print(len(User.objects.all().filter(username = request.POST['username'])))
        if len(User.objects.all().filter(username = request.POST['username'])) == 1:
            errors.append('用户名已被使用')

        if errors:
            return render(request,'res.html',{'errors':errors})

        account = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(account,'xx@qq.com',password)
        user.save()
        
        

        if request.POST['type'] == '1':
            userlogin = auth.authenticate(username = account,password = password)
            auth.login(request,userlogin)
            
            image = request.FILES['business_license_pic']

            # set user
            user.is_active = True
            user.is_staff = True
            user.groups.add(Group.objects.get(name='企业用户'))
            user.save()

            # set company
            need_data = ['name','credit_code','phone','incubator']
            dic = {  da:request.POST[da]    for da in request.POST if da in need_data}
            # print(dic['incubator'])
            dic['incubator'] = Incubator.objects.get(name=dic['incubator'])
            com = CompanyInfo.objects.create(status=0,business_license_pic=image,**dic,user=user)
            com.save()
            # FinancialSituation.objects.create(companyInfo=com)
            # ProductsAndMarket.objects.create(companyInfo=com)
            # TechnologyRD.objects.create(companyInfo=com)
            # ServerRequest.objects.create(companyInfo=com)
            return HttpResponseRedirect('/admin')

        elif request.POST['type'] == '2':

            user.is_active = True
            user.is_staff = True
            user.groups.add(Group.objects.get(name='孵化器用户'))
            user.save()
            need_data = ['name','phone']
            dic = {  da:request.POST[da]    for da in request.POST if da in need_data}
            inc = Incubator.objects.create(user=user,**dic)
            return HttpResponseRedirect('/admin/auth/user/')

        elif request.POST['type'] == '3':

            user.is_active = True
            user.is_staff = True
            user.groups.add(Group.objects.get(name='机构用户'))
            user.save()
            need_data = ['name','phone']
            dic = {  da:request.POST[da]    for da in request.POST if da in need_data}
            inc = Institution.objects.create(user=user,type=1,**dic)
            return HttpResponseRedirect('/admin/auth/user/')

        elif request.POST['type'] == '4':

            user.is_active = True
            user.is_staff = True
            user.groups.add(Group.objects.get(name='机构用户'))
            user.save()
            need_data = ['name','phone']
            dic = {  da:request.POST[da]    for da in request.POST if da in need_data}
            inc = Institution.objects.create(user=user,type=2,**dic)
            return HttpResponseRedirect('/admin/auth/user/')
    if get_user_group(request,'super'):
        return render(request,'res.html',{'errors':errors,'issuper':True})


    incubators = Incubator.objects.all()
    return render(request,'res.html',{'errors':errors,'incubators':incubators,'issuper':False})

def savedata_view(request):
    import os
    os.system('mysqldump -uroot -pmissing evaluateg > evaluateg.sql')
    return HttpResponseRedirect('/admin')

# @csrf_exempt
# def register(request):
#     errors = []
#     account = None
#     password = None
#     password2 = None
#     email = None
#     CompareFlag = False

#     # pprint(User.objects.get(id=5).groups)
#     if request.method == 'POST':
#         if not request.POST.get('account'):
#             errors.append('用户名不能为空')
#         else:
#             account = request.POST.get('account')

#         if not request.POST.get('password'):
#             errors.append('密码不能为空')
#         else:
#             password = request.POST.get('password')
#         if not request.POST.get('password2'):
#             errors.append('确认密码不能为空')
#         else:
#             password2 = request.POST.get('password2')

#         # if not request.POST.get('email'):
#         #     errors.append('邮箱不能为空')
#         # else:
#         #     email = request.POST.get('email')

#         if password is not None:
#             if password == password2:
#                 CompareFlag = True
#             else:
#                 errors.append('两次输入密码不一致')

#         if account is not None and password is not None and password2 is not None and CompareFlag :
#             user = User.objects.create_user(account,'11@qq.com',password)
#             user.save()

#             userlogin = auth.authenticate(username = account,password = password)
#             auth.login(request,userlogin)
#             inital_data(user)
#             return HttpResponseRedirect('/admin')

#     incubators = Incubator.objects.all()
#     print(incubators)
#     print(len(incubators))
#     return render(request,'register.html', {'errors': errors,'incubators':incubators})

# def inital_data(user):
#     user.is_active = True
#     user.is_staff = True
#     user.groups.add(Group.objects.get(name='企业用户'))
#     user.save()

    
#     com = CompanyInfo.objects.create(user=user,name='请填写企业名称')
#     FinancialSituation.objects.create(companyInfo=com)
#     ProductsAndMarket.objects.create(companyInfo=com)
#     TechnologyRD.objects.create(companyInfo=com)
#     ServerRequest.objects.create(companyInfo=com)

# def inital_company_data(user):
#     user.is_active = True
#     user.is_staff = True
#     user.groups.add(Group.objects.get(name='企业用户'))
#     user.save()

    
#     com = CompanyInfo.objects.create(user=user,name='请填写企业名称')
#     FinancialSituation.objects.create(companyInfo=com)
#     ProductsAndMarket.objects.create(companyInfo=com)
#     TechnologyRD.objects.create(companyInfo=com)
#     ServerRequest.objects.create(companyInfo=com)



# 用户登录
# @csrf_exempt
def my_login(request):
    # print(1111111111)
    errors =[]
    username = None
    password = None
    nn = 111100111
    if request.method == "POST":
        print(123)
        nn = 11122
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
    print(nn)
    return render(request,'login.html', {'errors': errors})

# 用户退出
# def my_logout(request):
#     auth.logout(request)
#     return HttpResponseRedirect('/blog')


def save_permission():
    gobjs = Group.objects.all()
    filename = 'permissionsmy.txt'
    if gobjs:
        print('保存了权限')
        datalst = []
        for gobj in gobjs:
            data = Permission.objects.filter(group=gobj).values('codename')
            for da in data:
                datalst.append(gobj.name+','+da['codename'])
        with open(filename,'w',encoding='utf-8') as f:
            f.write('\n'.join(datalst))
    else:
        print('读取了权限')
        with open(filename,'r',encoding='utf-8') as f:
            data = f.read()
        permissions = data.split()
        for permission in permissions:
            group_name,codename = permission.strip().split(',')
            try:
                gobj = Group.objects.get(name=group_name)
            except:
                gobj = Group.objects.create(name=group_name)
            gobj.permissions.add(Permission.objects.get(codename=codename))
            gobj.save()



# save_permission()
# 
# 
# 
