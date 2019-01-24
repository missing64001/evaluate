from django.shortcuts import render,redirect

# Create your views here.
from django.contrib import auth,admin
from django.contrib.auth.models import User,Group,Permission
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.http import StreamingHttpResponse
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
from django.contrib import messages
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
def my_staff(request):
    if request.user.is_authenticated() and not request.user.is_staff:
        return render(request,'staff.html')
    else:
        return HttpResponseRedirect('/admin/')


def MyAdminIndex(request):

    if request.user.is_authenticated() and not request.user.is_staff:
        return HttpResponseRedirect('/admin/staff/')

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

def my_register_in(request):
     return render(request,'res_incubator_institution.html') #{'errors':errors}

def my_register(request):
    errors = []
    incubators = Incubator.objects.all()
    if request.method == 'POST':



        if request.POST['password'] != request.POST['password2']:
            errors.append('两次输入密码不一致')

        if len(request.POST['password2']) < 6:
            errors.append('密码小于六位')

        # print(len(User.objects.all().filter(username = request.POST['username'])))
        if len(User.objects.all().filter(username = request.POST['username'])) == 1:
            errors.append('用户名已被使用')

        if request.POST.get('credit_code') and len(request.POST['credit_code']) != 18:
            errors.append('请填写正确的统一社会信用代码（18位）')


        if request.POST['type'] == '1':
            if CompanyInfo.objects.filter(name=request.POST['name']):
                errors.append('企业名称已被使用')
        elif request.POST['type'] == '2':
            if Incubator.objects.filter(name=request.POST['name']):
                errors.append('名称已被使用')
        elif request.POST['type'] in '34':
            if Institution.objects.filter(name=request.POST['name']):
                errors.append('名称已被使用')



        if errors and get_user_group(request) != 'super':
            errors = ['　　'.join(errors)]
            return render(request,'res.html',{'errors':errors,'incubators':incubators,'issuper':False})

        elif get_user_group(request) == 'super':
            if not request.POST['username']:
                errors.append('请输入用户名')

            if errors:
                messages.error(request, '\n'.join(errors))
                return HttpResponseRedirect('/admin/auth/user/res_in')


        account = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(account,'xx@qq.com',password)
        user.save()
        
        

        if request.POST['type'] == '1':
            if CompanyInfo.objects.filter(name=request.POST['name']):
                return render(request,'res.html',{'errors':'企业名称已被使用','incubators':incubators,'issuper':False})
            userlogin = auth.authenticate(username = account,password = password)
            auth.login(request,userlogin)
            
            image = request.FILES['business_license_pic']

            # set user
            user.is_active = True
            user.is_staff = False
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
def my_logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/admin')

def derive_data_view(request):
    if not get_user_group(request,'super'):
        return HttpResponseRedirect('/admin')
    print('导出数据')

    import xlwt
    workbook = xlwt.Workbook(encoding = 'utf-8')
    worksheet = workbook.add_sheet('企业信息')
    


    cobjs = CompanyInfo.objects.all()
    str_ = [
        '状态',
        '所属孵化器',
        '企业名称',
        '成立时间',
        '注册资本（万元）',
        '实收资本（万元）',
        '主营产品（或服务）',
        '职工总数',
        '大专以上学历人数',
        '从事研发人员数',
        '是否是高新技术企业',
        '企业简介',
        '行业领域',
        '二级领域',
        '统一社会信用代码',
        '联系电话',
        '-',
        '技术来源',
        '成果转化来源',
        '三、产品与市场',
        '主营产品（或服务）',
        '商业模式',
        '市场分析及前景预测',
        '四、技术与研发',
        '核心技术及研发情况',
        '五、服务需求',
        '融资金额（万元）',
        '融资时间（天）',
        '拟出让股权比例（%）',
        '可以接受的最高年利率（%）',
        '资金使用计划',
        '小额贷款（万元）',
        '股改、挂牌、上市',
        '科技金融服务需求',
        '其他科技服务需求',
        ]
    for i,s in enumerate(str_):
        worksheet.write(0, i, label = s)


    for i,cobj in enumerate(cobjs,1):
        try:
            otherm = Otherm.objects.get(companyInfo=cobj)
            othermlst = [otherm.get_x1_display(),
                otherm.get_technical_source_display(),
                otherm.get_SOAT_display(),]
        except Exception:
            othermlst = ['-','-','-',]

        try:
            productsandmarket = ProductsAndMarket.objects.get(companyInfo=cobj)
            productsandmarketlst = ['      |',productsandmarket.product,productsandmarket.model,productsandmarket.analysis_forecast,]
        except Exception:
            productsandmarketlst = ['      |','-','-','-',]

        try:
            technologyrd = TechnologyRD.objects.get(companyInfo=cobj)
            technologyrdlst = ['      |',technologyrd.status]
        except Exception:
            technologyrdlst = ['      |','-']

        try:
            serverrequest = ServerRequest.objects.get(companyInfo=cobj)
            serverrequestlst = ['      |',
                                serverrequest.amount,
                                serverrequest.duration,
                                serverrequest.ratio,
                                serverrequest.interest_rate,
                                serverrequest.plan,
                                serverrequest.small_loan,
                                serverrequest.get_share_model_display(),
                                serverrequest.request,
                                serverrequest.otherrequest,
            ]
        except Exception:
            serverrequestlst = ['      |','-','-','-','-','-','-','-','-','-']
            # import traceback
            # traceback.print_exc()






        # ServerRequest

        lst = [
                cobj.get_status_display(),
                cobj.incubator,
                cobj.name,
                cobj.create_date,
                cobj.registered_capital,
                cobj.paid_in_capital,
                cobj.major_business,
                cobj.work_force,
                cobj.junior_college_number,
                cobj.developer_number,
                cobj.is_high_tech_enterprise,
                cobj.abouts,
                cobj.get_field_1_display(),
                cobj.field_2,
                cobj.credit_code,
                cobj.phone,

                ]
        lst += othermlst
        lst += productsandmarketlst
        lst += technologyrdlst
        lst += serverrequestlst




        for j,l in enumerate(lst):
            l = str(l).replace('\n','\t').replace(',','，')
            if l == 'None':
                l = '-'
            worksheet.write(i, j, label = l)












    # ----------------------孵化器----------------------
    # ----------------------孵化器----------------------
    worksheet = workbook.add_sheet('孵化器')
    str_ = ['名称','联系电话','企业数量']

    objs = Incubator.objects.all().order_by('name')
    for i,s in enumerate(str_):
        worksheet.write(0, i, label = s)
            


    for i,obj in enumerate(objs,1):

        lst = [
        obj.name,
        obj.phone,
        len(CompanyInfo.objects.all().filter(incubator=obj)),
        ]

        for j,l in enumerate(lst):

            l = str(l).replace('\n','\t').replace(',','，')
            if l == 'None':
                l = '-'
            worksheet.write(i, j, label = l)
    
    # ----------------------孵化器----------------------
    # ----------------------孵化器------------------




    # ----------------------机构----------------------
    # ----------------------机构----------------------
    worksheet = workbook.add_sheet('机构')
    str_ = ['机构名称','机构类型','联系电话']

    objs = Institution.objects.all().order_by('name')
    for i,s in enumerate(str_):
        worksheet.write(0, i, label = s)
            


    for i,obj in enumerate(objs,1):

        lst = [
        obj.name,
        obj.get_type_display(),
        obj.phone,
        ]

        for j,l in enumerate(lst):

            l = str(l).replace('\n','\t').replace(',','，')
            if l == 'None':
                l = '-'
            worksheet.write(i, j, label = l)
    
    # ----------------------机构----------------------
    # ----------------------机构------------------






    # ----------------------二、财务状况----------------------
    # ----------------------二、财务状况----------------------
    worksheet = workbook.add_sheet('二、财务状况')
    str_ = ['企业','年份','累计销售收入','累计净利润','期末总资产','研发费用总额']

    objs = FinancialSituation.objects.all().order_by('companyInfo__name')
    for i,s in enumerate(str_):
        worksheet.write(0, i, label = s)
            


    for i,obj in enumerate(objs,1):

        lst = [
        obj.companyInfo,
        obj.year,
        obj.income,
        obj.profit,
        obj.total,
        obj.r_d_cost,
        ]

        for j,l in enumerate(lst):

            l = str(l).replace('\n','\t').replace(',','，')
            if l == 'None':
                l = '-'
            worksheet.write(i, j, label = l)
    
    # ----------------------二、财务状况----------------------
    # ----------------------二、财务状况------------------



    # ----------------------主要股东及股权比例（前五名）----------------------
    # ----------------------主要股东及股权比例（前五名）----------------------
    worksheet = workbook.add_sheet('主要股东及股权比例（前五名）')

    str_ = ['企业','股东名称','股权比例(%)','出资形式']

    objs = Shareholder.objects.all().order_by('companyInfo__name')
    for i,s in enumerate(str_):
        worksheet.write(0, i, label = s)
            
    for i,obj in enumerate(objs,1):


        # try:
        #     shareholder = Shareholder.objects.get(companyInfo=cobj)
        #     shareholderlst = [shareholder.name,shareholder.share_ratio,shareholder.form_of_contribution]
        # except Exception:
        #     shareholderlst = ['-','-','-',]

        lst = [obj.companyInfo,obj.name,obj.share_ratio,obj.form_of_contribution]

        for j,l in enumerate(lst):

            l = str(l).replace('\n','\t').replace(',','，')
            if l == 'None':
                l = '-'
            worksheet.write(i, j, label = l)
    
    # ----------------------主要股东及股权比例（前五名）----------------------
    # ----------------------主要股东及股权比例（前五名）----------------------




    # ----------------------企业获奖情况----------------------
    # ----------------------企业获奖情况----------------------
    worksheet = workbook.add_sheet('企业获奖情况')
    str_ = ['企业','获奖级别','获奖名称','获奖时间']

    objs = EnterpriseAwards.objects.all().order_by('companyInfo__name')
    for i,s in enumerate(str_):
        worksheet.write(0, i, label = s)
            


    for i,obj in enumerate(objs,1):

        lst = [obj.companyInfo,obj.level,obj.title,obj.date]

        for j,l in enumerate(lst):

            l = str(l).replace('\n','\t').replace(',','，')
            if l == 'None':
                l = '-'
            worksheet.write(i, j, label = l)
    
    # ----------------------企业获奖情况----------------------
    # ----------------------企业获奖情况----------------------


    # ----------------------核心团队个人获奖情况----------------------
    # ----------------------核心团队个人获奖情况----------------------
    worksheet = workbook.add_sheet('核心团队个人获奖情况')
    str_ = ['企业','获奖人','获奖级别/名称','获奖时间']

    objs = PersonalAwards.objects.all().order_by('companyInfo__name')
    for i,s in enumerate(str_):
        worksheet.write(0, i, label = s)
            


    for i,obj in enumerate(objs,1):

        lst = [obj.companyInfo,obj.name,obj.level_title,obj.date]

        for j,l in enumerate(lst):

            l = str(l).replace('\n','\t').replace(',','，')
            if l == 'None':
                l = '-'
            worksheet.write(i, j, label = l)
    
    # ----------------------核心团队个人获奖情况----------------------
    # ----------------------核心团队个人获奖情况----------------------



    # ----------------------企业曾经承担或正在承担的科技计划项目----------------------
    # ----------------------企业曾经承担或正在承担的科技计划项目----------------------
    worksheet = workbook.add_sheet('企业曾经承担或正在承担的科技计划项目')
    str_ = ['企业','计划类别','立项名称','立项时间','结项时间','结论']

    objs = Project.objects.all().order_by('companyInfo__name')
    for i,s in enumerate(str_):
        worksheet.write(0, i, label = s)
            


    for i,obj in enumerate(objs,1):

        lst = [obj.companyInfo,
                obj._type,
                obj.title,
                obj.create_date,
                obj.finished_date,
                obj.conclusion]

        for j,l in enumerate(lst):

            l = str(l).replace('\n','\t').replace(',','，')
            if l == 'None':
                l = '-'
            worksheet.write(i, j, label = l)
    
    
    # ----------------------企业曾经承担或正在承担的科技计划项目----------------------
    # ----------------------企业曾经承担或正在承担的科技计划项目----------------------



    # ----------------------专利----------------------
    # ----------------------专利----------------------
    worksheet = workbook.add_sheet('专利')
    str_ = ['企业','专利名','专利类型','专利号','获得时间']

    objs = Patent.objects.all().order_by('companyInfo__name')
    for i,s in enumerate(str_):
        worksheet.write(0, i, label = s)
            


    for i,obj in enumerate(objs,1):

        lst = [obj.companyInfo,
                obj.title,
                obj._type,
                obj.num,
                obj.date,
                ]

        for j,l in enumerate(lst):

            l = str(l).replace('\n','\t').replace(',','，')
            if l == 'None':
                l = '-'
            worksheet.write(i, j, label = l)
    
    
    # ----------------------专利----------------------
    # ----------------------专利----------------------
    




    # ----------------------药品批文----------------------
    # ----------------------药品批文----------------------
    worksheet = workbook.add_sheet('药品批文')
    str_ = ['企业','药品名称','国家新药','国家一级中药保护品种','药品批准文号','有效日期']

    objs = DrugApproval.objects.all().order_by('companyInfo__name')
    for i,s in enumerate(str_):
        worksheet.write(0, i, label = s)
            


    for i,obj in enumerate(objs,1):

        lst = [obj.companyInfo,
                obj.title,
                obj.new_drug,
                obj.c_drug,
                obj.num,
                obj.effective_date,
                ]

        for j,l in enumerate(lst):

            l = str(l).replace('\n','\t').replace(',','，')
            if l == 'None':
                l = '-'
            worksheet.write(i, j, label = l)
    
    
    # ----------------------药品批文----------------------
    # ----------------------药品批文----------------------
    



    # ----------------------医疗器械注册证----------------------
    # ----------------------医疗器械注册证----------------------
    worksheet = workbook.add_sheet('医疗器械注册证')
    str_ = ['企业','产品名称','医疗器械注册号','有效日期']

    objs = MIRC.objects.all().order_by('companyInfo__name')
    for i,s in enumerate(str_):
        worksheet.write(0, i, label = s)
            


    for i,obj in enumerate(objs,1):

        lst = [obj.companyInfo,
                obj.title,
                obj.num,
                obj.effective_date,
                ]

        for j,l in enumerate(lst):

            l = str(l).replace('\n','\t').replace(',','，')
            if l == 'None':
                l = '-'
            worksheet.write(i, j, label = l)
    
    
    # ----------------------医疗器械注册证----------------------
    # ----------------------医疗器械注册证----------------------
    



    # ----------------------标准制定情况----------------------
    # ----------------------标准制定情况----------------------
    worksheet = workbook.add_sheet('标准制定情况')
    str_ = ['企业','标准名称','标准级别','标准编号','起草单位中的地位']

    objs = StandardSetting.objects.all().order_by('companyInfo__name')
    for i,s in enumerate(str_):
        worksheet.write(0, i, label = s)
            


    for i,obj in enumerate(objs,1):

        lst = [obj.companyInfo,
                obj.title,
                obj.level,
                obj.num,
                obj.status,
                ]

        for j,l in enumerate(lst):

            l = str(l).replace('\n','\t').replace(',','，')
            if l == 'None':
                l = '-'
            worksheet.write(i, j, label = l)
    
    
    # ----------------------标准制定情况----------------------
    # ----------------------标准制定情况----------------------
    



    # ----------------------  核心团队（至少填三人）----------------------
    # ----------------------  核心团队（至少填三人）----------------------
    worksheet = workbook.add_sheet('核心团队')
    str_ = ['企业','姓名','性别','年龄','职位','留学经历','创业次数','谈对自己创业最重要的一个经历',
            '学历','毕业院校','专业','学历','毕业院校','专业','学历','毕业院校','专业',
            '工作单位','职位','开始','结束','工作单位','职位','开始','结束','工作单位','职位','开始','结束',]

    objs = CoreMember.objects.all().order_by('companyInfo__name')
    for i,s in enumerate(str_):
        worksheet.write(0, i, label = s)
            


    for i,obj in enumerate(objs,1):

        lst = [obj.companyInfo,
                obj.name,
                obj.gender,
                obj.age,
                obj.position,
                obj.is_study_abroad,
                obj.entrepreneurial_times,
                obj.experience,

                obj.education1,
                obj.university1,
                obj.major1,
                obj.education2,
                obj.university2,
                obj.major2,
                obj.education3,
                obj.university3,
                obj.major3,

                obj.company1,
                obj.position1,
                obj.date_s1,
                obj.date_e1,
                obj.company2,
                obj.position2,
                obj.date_s2,
                obj.date_e2,
                obj.company3,
                obj.position3,
                obj.date_s3,
                obj.date_e3,
                ]

        for j,l in enumerate(lst):

            l = str(l).replace('\n','\t').replace(',','，')
            if l == 'None':
                l = '-'
            worksheet.write(i, j, label = l)
    
    
    # ----------------------  核心团队（至少填三人）----------------------
    # ----------------------  核心团队（至少填三人）----------------------
    








    workbook.save('data.xls')



    """查询数据下载"""
    def file_iterator(file_name, chunk_size=512):
        with open(file_name, 'rb') as f:
            while True:
                c = f.read(chunk_size)
                # print(c)
                if c:
                    yield c
                else:
                    break
    the_file_name = 'data.xls'
    response = StreamingHttpResponse(file_iterator(the_file_name))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)
    return response


def derive_data_view_old(request):
    if not get_user_group(request,'super'):
        return HttpResponseRedirect('/admin')
    print('导出数据')

    import xlwt
    workbook = xlwt.Workbook(encoding = 'utf-8')
    worksheet = workbook.add_sheet('企业信息')
    worksheet.write(0, 0, label = 'Row 0, Column 0 Value')


    cobjs = CompanyInfo.objects.all()
    str_ = [
        '企业名称',
        '状态',
        '所属孵化器',
        '成立时间',
        '注册资本（万元）',
        '实收资本（万元）',
        '主营产品（或服务）',
        '职工总数',
        '大专以上学历人数',
        '从事研发人员数',
        '是否是高新技术企业',
        '企业简介',
        '行业领域',
        '二级领域',
        '统一社会信用代码',
        '联系电话',]


    strlst = [','.join(str_)]
    for cobj in cobjs:
        lst = [
                cobj.name,
                cobj.get_status_display(),
                cobj.incubator,
                cobj.create_date,
                cobj.registered_capital,
                cobj.paid_in_capital,
                cobj.major_business,
                cobj.work_force,
                cobj.junior_college_number,
                cobj.developer_number,
                cobj.is_high_tech_enterprise,
                cobj.abouts,
                cobj.get_field_1_display(),
                cobj.field_2,
                cobj.credit_code,
                cobj.phone,]
        lst = [ str(l).replace('\n','\t').replace(',','，') for l in lst]

        strlst.append(','.join(lst))

    for str_ in strlst:
        print(type(str_))
    filename = 'derive_data.csv'
    with open(filename,'w',encoding='utf-8') as f:
        f.write('\n'.join(strlst))


    return HttpResponseRedirect('/admin')

def redeclare_view(request):
    cid = request.GET.get('cid')
    print(cid)
    cobj = CompanyInfo.objects.get(id=cid)
    if cobj.status == 10:
        cobj.status = 0
    css = CompanyStatus.objects.filter(companyInfo=cobj)
    for cs in css:
        cs.is_alive=False
        cs.save()
    cobj.save()
    CompanyStatus.objects.create(companyInfo=cobj,status=0)
    return HttpResponseRedirect('/admin/company/companyinfo')


def set_permission(request):
    if not get_user_group(request.user,'super'):
        return HttpResponseRedirect('/admin/')
    type_ = request.GET['type']
    gobjs = Group.objects.all()
    filename = 'permissionsmy.txt'
    if type_ == 'save':
        print('保存了权限')
        datalst = []
        for gobj in gobjs:
            data = Permission.objects.filter(group=gobj).values('codename')
            for da in data:
                datalst.append(gobj.name+','+da['codename'])
        with open(filename,'w',encoding='utf-8') as f:
            f.write('\n'.join(datalst))

    elif type_ == 'load':
        print('读取了权限')
        with open(filename,'r',encoding='utf-8') as f:
            data = f.read()
        permissions = data.split('\n')
        for permission in permissions:
            group_name,codename = permission.strip().split(',')
            try:
                gobj = Group.objects.get(name=group_name)
            except Group.DoesNotExist:
                gobj = Group.objects.create(name=group_name)
            try:
                gobj.permissions.add(Permission.objects.get(codename=codename))
                gobj.save()
            except Exception:
                pass

        print('读取权限完成')
    return HttpResponseRedirect('/admin')


# save_permission()
# 
# 
# 
