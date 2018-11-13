from django.contrib import admin
from .models import *
from incubator.models import Incubator
from django.utils.html import format_html
from institution.models import *
from django.db.models import Max




class ShareholderInl(admin.StackedInline):
    model = Shareholder
    extra = 0
    max_num = 5
    def get_readonly_fields(self, request,obj=None):
        
        if get_user_group(request,'企业用户'):
            status = CompanyInfo.objects.get(user=request.user).status
            if status == 5 or status < 4:
                return []
        return ('name','share_ratio','form_of_contribution')

class EnterpriseAwardsInl(admin.StackedInline):
    model = EnterpriseAwards
    extra = 0
    max_num = 5
    def get_readonly_fields(self, request,obj=None):
        if get_user_group(request,'企业用户'):
            status = CompanyInfo.objects.get(user=request.user).status
            if status == 5 or status < 4:
                return []
        return ('level','title','date')


class PersonalAwardsInl(admin.StackedInline):
    model = PersonalAwards
    extra = 0
    max_num = 5
    def get_readonly_fields(self, request,obj=None):
        if get_user_group(request,'企业用户'):
            status = CompanyInfo.objects.get(user=request.user).status
            if status == 5 or status < 4:
                return []
        return ('name','level_title','date')

class ProjectInl(admin.StackedInline):
    model = Project
    extra = 0
    max_num = 5
    def get_readonly_fields(self, request,obj=None):
        if get_user_group(request,'企业用户'):
            status = CompanyInfo.objects.get(user=request.user).status
            if status == 5 or status < 4:
                return []
        return ('_type','title','create_date','finished_date','conclusion')
    
class PatentInl(admin.StackedInline):
    model = Patent
    extra = 0
    max_num = 5
    def get_readonly_fields(self, request,obj=None):
        if get_user_group(request,'企业用户'):
            status = CompanyInfo.objects.get(user=request.user).status
            if status == 5 or status < 4:
                return []
        return ('title','_type','num','date')
    
class DrugApprovalInl(admin.StackedInline):
    model = DrugApproval
    extra = 0
    max_num = 5    
    def get_readonly_fields(self, request,obj=None):
        if get_user_group(request,'企业用户'):
            status = CompanyInfo.objects.get(user=request.user).status
            if status == 5 or status < 4:
                return []
        return ('title','new_drug','c_drug','num','effective_date')

class MIRCInl(admin.StackedInline):
    model = MIRC
    extra = 0
    max_num = 5    
    def get_readonly_fields(self, request,obj=None):
        if get_user_group(request,'企业用户'):
            status = CompanyInfo.objects.get(user=request.user).status
            if status == 5 or status < 4:
                return []
        return ('title','num','effective_date')

class StandardSettingInl(admin.StackedInline):
    model = StandardSetting
    extra = 0
    max_num = 5
    def get_readonly_fields(self, request,obj=None):
        if get_user_group(request,'企业用户'):
            status = CompanyInfo.objects.get(user=request.user).status
            if status == 5 or status < 4:
                return []
        return ('title','level','num','status')

# class CoreMemberInl(admin.StackedInline):
#     model = CoreMember
#     extra = 0
#     max_num = 5
#     readonly_fields = ('title','level','num','status')

class EducationExperienceInl(admin.StackedInline):
    model = EducationExperience
    extra = 1
    max_num = 5

class WorkExperienceInl(admin.StackedInline):
    model = WorkExperience
    extra = 1
    max_num = 5
    # def get_readonly_fields(self, request,obj=None):
    #             status = CompanyInfo.objects.get(user=request.user).status
        # if get_user_group(request,'企业用户') and (status == 5 or status < 4):
    #         return []
    #     return ('year','income','profit','total','r_d_cost')

class FinancialSituationInl(admin.StackedInline):
    model = FinancialSituation
    extra = 0
    max_num = 5
    def get_readonly_fields(self, request,obj=None):
        if get_user_group(request,'企业用户'):
            status = CompanyInfo.objects.get(user=request.user).status
            if status == 5 or status < 4:
                return []
        return ('year','income','profit','total','r_d_cost')

class ProductsAndMarketInl(admin.StackedInline):
    model = ProductsAndMarket
    extra = 1
    # max_num = 5
    def get_readonly_fields(self, request,obj=None):
        if get_user_group(request,'企业用户'):
            status = CompanyInfo.objects.get(user=request.user).status
            if status == 5 or status < 4:
                return []
        return ('product','model','analysis_forecast')

class TechnologyRDInl(admin.StackedInline):
    model = TechnologyRD
    extra = 1
    # max_num = 5
    def get_readonly_fields(self, request,obj=None):
        if get_user_group(request,'企业用户'):
            status = CompanyInfo.objects.get(user=request.user).status
            if status == 5 or status < 4:
                return []
        return ('status',)

class ServerRequestInl(admin.StackedInline):
    model = ServerRequest
    extra = 1
    # max_num = 5
    def get_readonly_fields(self, request,obj=None):
        if get_user_group(request,'企业用户'):
            status = CompanyInfo.objects.get(user=request.user).status
            if status == 5 or status < 4:
                return []
        return ('amount','duration','ratio','interest_rate','plan','small_loan','share_model','request','otherrequest')


class OthermInl(admin.StackedInline):
    model = Otherm
    extra = 1
    # max_num = 5
    def get_readonly_fields(self, request,obj=None):
        if get_user_group(request,'企业用户'):
            status = CompanyInfo.objects.get(user=request.user).status
            if status == 5 or status < 4:
                return []
        return ('x1','technical_source','SOAT')

class CoreMemberInl(admin.StackedInline):
    model = CoreMember
    extra = 0
    # max_num = 5
    fields =('name','gender','age','position','is_study_abroad','entrepreneurial_times','experience',
        ('xxtemp1','education1','university1','major1'),
        ('xxtemp2','education2','university2','major2'),
        ('xxtemp3','education3','university3','major3'),
        ('xxtempgz1','company1','position1','date_s1','date_e1'),
        ('xxtempgz2','company2','position2','date_s2','date_e2'),
        ('xxtempgz3','company3','position3','date_s3','date_e3'),
        )

    def get_readonly_fields(self, request,obj=None):
        if get_user_group(request,'企业用户'):
            status = CompanyInfo.objects.get(user=request.user).status
            if status == 5 or status < 4:
                return []
        return ('name','gender','age','position','is_study_abroad','entrepreneurial_times','experience',
                'xxtemp1','education1','university1','major1',
                'xxtemp2','education2','university2','major2',
                'xxtemp3','education3','university3','major3',
                'company1','position1','date_s1','date_e1',
                'company2','position2','date_s2','date_e2',
                'company3','position3','date_s3','date_e3',
                )


# @admin.register(CoreMember)
# class CoreMemberAdmin(admin.ModelAdmin):
#     inlines = [EducationExperienceInl,WorkExperienceInl]
#     exclude = ('companyInfo',)

#     def get_queryset(self, request):
#         qs = super().get_queryset(request)
#         if request.user.is_superuser:
#             return qs
#         companyInfo = CompanyInfo.objects.filter(user=request.user)
#         print(companyInfo.count())
#         return qs.filter(companyInfo=companyInfo)






@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display=['name','phone','incubator','credit_code','business_license_pic_show','new_status']
    search_fields = ('name','incubator__name')
    inlines = [ShareholderInl, EnterpriseAwardsInl,PersonalAwardsInl,ProjectInl,PatentInl,
                DrugApprovalInl,MIRCInl,StandardSettingInl,OthermInl,CoreMemberInl,FinancialSituationInl
                ,ProductsAndMarketInl,TechnologyRDInl,ServerRequestInl] #CoreMemberInl,
    exclude = ('user','credit_code','phone','business_license_pic','status')

    # fieldsets = (

    #     (   

    #         '基本选项',{
    #             'fields':('incubator',('name','create_date'),('registered_capital','paid_in_capital'),
    #                 ('major_business','work_force'),('junior_college_number','developer_number'),
    #                 'is_high_tech_enterprise','abouts','field_1','field_2','x1','technical_source','SOAT'),
    #         }
    #     ),
    # )

    # fieldsets = (

    #     (   

    #         '基本选项',{
    #             'fields':('ShareholderInl','EnterpriseAwardsInl'),
    #         }
    #     ),
    # )

    # def get_inline_instances(self, request, obj=None):
    #     inline_instances = []
    #     if get_user_group(request,'孵化器用户'):
    #         inlines = self.inlines + [FinancialSituationInl,ProductsAndMarketInl,TechnologyRDInl,ServerRequestInl]
    #     else:
    #         inlines = self.inlines

    #     for inline_class in inlines:
    #         inline = inline_class(self.model, self.admin_site)
    #         if request:
    #             if not (inline.has_add_permission(request) or
    #                     inline.has_change_permission(request, obj) or
    #                     inline.has_delete_permission(request, obj)):
    #                 continue
    #             if not inline.has_add_permission(request):
    #                 inline.max_num = 0
    #         inline_instances.append(inline)

    #     return inline_instances

    # def info_status(self,obj):
    #     return 'need set'
    # info_status.short_description = '企业状态'

    # def get_inline_instances(self, request,obj=None):
    #     inlines = [ShareholderInl, EnterpriseAwardsInl,PersonalAwardsInl,ProjectInl,PatentInl,
    #             DrugApprovalInl,MIRCInl,StandardSettingInl,

    #     return inlines

    def get_user_group_1(self,obj):
        return format_html('''<span class="get_user_group">机构用户</span> <script type="text/javascript" src="/static/js/set_head.js"></script>''')

    def get_readonly_fields(self, request,obj=None):
        status = 0
        if get_user_group(request,'企业用户'):
            status = CompanyInfo.objects.get(user=request.user).status
        elif get_user_group(request,'super'):
            status = obj.status
        
        if get_user_group(request,'孵化器用户') or status == 4 or status > 5:
            return ('incubator','name','create_date','registered_capital','paid_in_capital',
                'major_business','work_force','junior_college_number','developer_number','is_high_tech_enterprise'
                ,'abouts','field_1','field_2') # ,'x1','technical_source','SOAT'
        if get_user_group(request,'机构用户'):
            return ('incubator','name','create_date','registered_capital','paid_in_capital',
                'major_business','work_force','junior_college_number','developer_number','is_high_tech_enterprise'
                ,'abouts','field_1','field_2','get_user_group_1') # ,'x1','technical_source','SOAT'
        return []

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        elif get_user_group(request,'孵化器用户'):
            return qs.filter(incubator=Incubator.objects.get(user=request.user))
        elif get_user_group(request,'机构用户'):
            return qs.filter(investreport__institution__user=request.user).annotate(Max('id'))
            # return investreport.filter(institution=Institution.objects.get(user=request.user)).companyInfo

            
        return qs.filter(user=request.user)

    def save_model(self, request, obj, form, change):
        try:
            if obj.status == 0:
                if obj.financialsituation_set and obj.productsandmarket and obj.technologyrd and obj.serverrequest:
                    obj.status = 1
            obj.save()
        except Exception:
            obj.save()

    def new_status(self,obj):
        status_choices = ((-2,'无效'),
                        (-1,'完成'),
                        (0,'通过申请'),
                        (1,'填写企业信息完成'),
                        (2,'上传财务报表完成'),
                        (3,'企业自我评价完成'),
                        (4,'已提交'),

                        (5,'孵化器驳回信息'), #修改后确认提交
                        (6,'孵化器审核信息'),
                        (7,'孵化器修正评价'),

                        (8,'平台发送报告'),

                        (9,'机构反馈报告'),

                        (10,'用户获得反馈'),
                    )
        status_choices = dict(status_choices)
        report = status_choices[obj.status]

        if obj.status == 4:
            report = format_html("<a style='font-weight:bold;' onclick='reject_company({})'>{}（如有问题点击驳回）</a>",obj.id,report)
        elif obj.status == 5:
            report = format_html("<a style='color:red;' onclick='reject_company({})'>已被驳回（如有问题可点击添加驳回原因）</a>",obj.id)
        if not obj.user.is_staff:
            report = format_html("<a style='color:red;' onclick='verify_company({})'>审核中（点击通过审核）</a>",obj.id)
        return report
    
    new_status.short_description = '状态'
    # class Media:        
    #     js = ('/static/js/balance.js',)

    def business_license_pic_show(self,obj):

        path = str(obj.business_license_pic)
        if not path.startswith('static/'):
            path = 'static/' + path
        return format_html('<div style="height: 50px;overflow: hidden;"><a href="/' + path + '" width=30 height=50 data-lightbox="' + path + '"><img src="/' + path + '" width=30 height=50" /></a></div>')
    business_license_pic_show.short_description = '营业执照'

    class Media:
        css = {'all': ('lightbox/css/lightbox.min.css',)}
        js = ('/static/js/company_fhq_prompt.js','lightbox/js/lightbox-plus-jquery.js')


    
@admin.register(FinancialSituation)
class FinancialSituationAdmin(admin.ModelAdmin):
    exclude = ('companyInfo',)
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(companyInfo=CompanyInfo.objects.get(user=request.user))
    
@admin.register(ProductsAndMarket)
class ProductsAndMarketAdmin(admin.ModelAdmin):
    exclude = ('companyInfo',)
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(companyInfo=CompanyInfo.objects.get(user=request.user))
    
@admin.register(TechnologyRD)
class TechnologyRDAdmin(admin.ModelAdmin):
    exclude = ('companyInfo',)
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(companyInfo=CompanyInfo.objects.get(user=request.user))


@admin.register(ServerRequest)
class ServerRequestAdmin(admin.ModelAdmin):
    exclude = ('companyInfo',)
    readonly_fields = ('amount',)
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(companyInfo=CompanyInfo.objects.get(user=request.user))


@admin.register(IndependentEvaluationOfEnterprises)
class IndependentEvaluationOfEnterprisesAdmin(admin.ModelAdmin):
    list_display=['companyInfo','external_environment','products_and_market','technology_R_D','team','create_date']
    # exclude = ('companyInfo',)
    search_fields = ('companyInfo__name',)
    readonly_fields = ('companyInfo',)
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if get_user_group(request,'super'):
            return qs
        elif get_user_group(request,'企业用户'):
            return qs.filter(companyInfo=CompanyInfo.objects.get(user=request.user))
        elif get_user_group(request,'孵化器用户'):
            return qs.filter(companyInfo__incubator=Incubator.objects.get(user=request.user))

    def get_readonly_fields(self,request,obj):
        if obj and obj.companyInfo.status > 3:
            return ('companyInfo','external_environment','products_and_market','technology_R_D','team')
        return self.readonly_fields

    def get_list_display(self, request, obj=None):
        if not get_user_group(request,'企业用户'):
            return ['companyInfo','external_environment_add','products_and_market_add','technology_R_D_add','team_add','create_date']
        return self.list_display

    class Media:
        js = ('/static/js/opt_evaluation.js',)

    def save_model(self, request, obj, form, change):
        obj.companyInfo = CompanyInfo.objects.get(user=request.user)
        obj.save()

        cobj = CompanyInfo.objects.get(user=request.user)
        if cobj.status == 2:
            cobj.status = 3
            cobj.save()

    def external_environment_add(self,obj):
        eobjs = EvaluationOfEnterprises.objects.filter(companyInfo=obj.companyInfo)
        if eobjs and eobjs[0].external_environment:
            return '%s分 （%s分）' % (eobjs[0].external_environment ,obj.external_environment)
        else:
            return '%s （%s分）' % ('--' ,obj.external_environment)

        
    def products_and_market_add(self,obj):
        eobjs = EvaluationOfEnterprises.objects.filter(companyInfo=obj.companyInfo)
        if eobjs and eobjs[0].products_and_market:
            return '%s分 （%s分）' % (eobjs[0].products_and_market ,obj.products_and_market)
        else:
            return '%s （%s分）' % ('--' ,obj.products_and_market)
        
    def technology_R_D_add(self,obj):
        eobjs = EvaluationOfEnterprises.objects.filter(companyInfo=obj.companyInfo)
        if eobjs and eobjs[0].technology_R_D:
            return '%s分 （%s分）' % (eobjs[0].technology_R_D ,obj.technology_R_D)
        else:
            return '%s （%s分）' % ('--' ,obj.technology_R_D)
        
    def team_add(self,obj):
        eobjs = EvaluationOfEnterprises.objects.filter(companyInfo=obj.companyInfo)
        if eobjs and eobjs[0].team:
            return '%s分 （%s分）' % (eobjs[0].team ,obj.team)
        else:
            return '%s （%s分）' % ('--' ,obj.team)

    external_environment_add.short_description = '企业所处外部环境（企业自评）'
    products_and_market_add.short_description = '企业主营产品及市场开拓（企业自评）'
    technology_R_D_add.short_description = '企业核心技术及研发实力（企业自评）'
    team_add.short_description = '企业经营及管理团队（企业自评）'
    # def change_view(self, request, object_id, form_url='', extra_context=None):
    #     return self.changeform_view(request, object_id, form_url, extra_context)





@admin.register(EvaluationOfEnterprises)
class EvaluationOfEnterprisesAdmin(admin.ModelAdmin):
    readonly_fields = ('companyInfo',)
    # def formfield_for_foreignkey(self, db_field, request, **kwargs):

    #     # if db_field.name == "car":
    #     #     kwargs["queryset"] = Car.objects.filter(owner=request.user)
    #     return super(EvaluationOfEnterprisesAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if get_user_group(request,'孵化器用户'):
            return qs.filter(companyInfo__incubator=Incubator.objects.get(user=request.user))

    def get_readonly_fields(self,request,obj):
        if obj.companyInfo.status > 6:
            return ('companyInfo','external_environment','products_and_market','technology_R_D','team')
        return self.readonly_fields

    # def formfield_for_dbfield(self, db_field, request, **kwargs):

    #     field =  super().formfield_for_dbfield(db_field, request, **kwargs)
    #     com = IndependentEvaluationOfEnterprises
    #     eobj = EvaluationOfEnterprises.objects.filter(companyInfo=obj.companyInfo)
    #     if db_field.name == 'external_environment':
    #         field.initial = True

    #     if db_field.name == 'groups':
    #         field.initial = request.GET['type']

    #     return field
    
    def save_model(self, request, obj, form, change):
        obj.companyInfo.status = 7
        obj.companyInfo.save()
        obj.save()


    class Media:
        js = ('/static/js/opt_evaluation.js',)
# EvaluationOfEnterprises




@admin.register(RejectReason)
class RejectReasonAdmin(admin.ModelAdmin):
    list_display = ['companyInfo','text','is_alive','create_date']
    search_fields = ('companyInfo__name', 'text')
    list_editable = ('is_alive',)



# @admin.register(Balance)
# class BalanceAdmin(admin.ModelAdmin):
#     def get_queryset(self, request):
#         qs = super().get_queryset(request)
#         if request.user.is_superuser:
#             return qs
#         return qs.filter(companyInfo=CompanyInfo.objects.get(user=request.user))
    

# admin.register(Shareholder)
# class ShareholderAdmin(admin.ModelAdmin):
#     pass


# Register your models here.
