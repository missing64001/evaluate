from django.contrib import admin
from .models import *
from incubator.models import Incubator
from django.utils.html import format_html
from institution.models import *
from django.db.models import Max,Count




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
    inl_index = 0
    # max_num = 5
    fields =['name','gender','age','position','is_study_abroad','entrepreneurial_times','experience',
        ('xxtemp1','education1','university1','major1'),
        ('xxtemp2','education2','university2','major2'),
        ('xxtemp3','education3','university3','major3'),
        ('xxtempgz1','company1','position1','date_s1','date_e1'),
        ('xxtempgz2','company2','position2','date_s2','date_e2'),
        ('xxtempgz3','company3','position3','date_s3','date_e3'),
        ]

    # def get_fields(self, request,obj=None):
    #     if get_user_group(request,'企业用户'):
    #         status = CompanyInfo.objects.get(user=request.user).status
    #         if status == 5 or status < 4:
    #             return self.fields
    #     obj = obj.coremember_set.all()[self.inl_index]
    #     self.inl_index += 1
    #     if not obj.education1:

    #         fieldsf = self.fields[:-6]
    #     elif not obj.education2:
    #         fieldsf = self.fields[:-5]
    #     elif not obj.education3:
    #         fieldsf = self.fields[:-4]
    #     else:
    #         fieldsf = self.fields[:-3]

    #     if not obj.company1:
    #         fieldsb = self.fields[-3:-3]
    #     elif not obj.company2:
    #         fieldsb = self.fields[-3:-2]
    #     elif not obj.company3:
    #         fieldsb = self.fields[-3:-1]
    #     else:
    #         fieldsb = self.fields[-3:]

    #     # print(fieldsf)
    #     # print(fieldsb)
    #     print(fieldsf + fieldsb)
    #     return fieldsf + fieldsb
        
    def get_readonly_fields(self, request,obj=None):
        if get_user_group(request,'企业用户'):
            status = CompanyInfo.objects.get(user=request.user).status
            if status == 5 or status < 4:
                return []
        return ('name','gender','age','position','is_study_abroad','entrepreneurial_times','experience',
                'education1','university1','major1',
                'education2','university2','major2',
                'education3','university3','major3',
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

    list_display=['name','phone','incubator','credit_code','business_license_pic_show']
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
    
    def get_list_display(self, request, obj=None):
        if get_user_group(request,'super'):
            self.list_editable = ('status',)
            return ['name','phone','incubator','credit_code','business_license_pic_show','status','livenesssuper']
        elif get_user_group(request,'孵化器用户'):
            return ['name','phone','incubator','credit_code','business_license_pic_show','new_status','liveness']
        else:
            return self.list_display

    # def get_list_editable(self, request, obj=None):
    #     print(1111111111)
    #     if get_user_group(request,'super'):
    #         return ('status',)
    #     return self.list_editable


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

        if get_user_group(request,'super'):
            return ('incubator','name','create_date','registered_capital','paid_in_capital',
                'major_business','work_force','junior_college_number','developer_number','is_high_tech_enterprise'
                ,'abouts','field_1','field_2','get_user_group_1') # ,'x1','technical_source','SOAT'
        return []

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs.filter(user__id__gt=0)
        elif get_user_group(request,'孵化器用户'):
            return qs.filter(incubator=Incubator.objects.get(user=request.user),user__id__gt=0)
        elif get_user_group(request,'机构用户'):
            return qs.filter(investreport__institution__user=request.user).annotate(Max('id'))
            # return investreport.filter(institution=Institution.objects.get(user=request.user)).companyInfo

            
        return qs.filter(user=request.user)

    def save_model(self, request, obj, form, change):
        try:
            if obj.status == 0:
                if obj.financialsituation_set and obj.productsandmarket and obj.technologyrd and obj.serverrequest:
                    obj.status = 1
                    if not CompanyStatus.objects.filter(companyInfo=obj,status=1):
                        CompanyStatus.objects.create(companyInfo=obj,status=1)
            obj.save()
        except Exception:
            obj.save()

    def new_status(self,obj):
        status_choices = ((-2,'无效'),
                        (-1,'完成'),
                        (0,'账号已激活'),
                        (1,'已填写企业信息'),
                        (2,'已上传财务报表'),
                        (3,'已完成自我评价'),
                        (4,'已提交企业信息'),

                        (5,'孵化器驳回信息'), #修改后确认提交
                        # (6,'孵化器已审核信息'),
                        (7,'孵化器已校正评价'),

                        (8,'已发送评估报告'),

                        (9,'机构已反馈报告'),

                        (10,'企业收到反馈信息'),
                    )

        status_choices = dict(status_choices)
        report = status_choices[obj.status]

        if obj.status == 4:
            report = format_html("<input style='width:140px' type='button' onclick='reject_company({})' value=驳回企业提交数据 >",obj.id) # ,report #<span style='font-size: 12px;'> {}（如有问题点击驳回）</sapn>
        elif obj.status == 5:
            report = format_html("<input style='width:140px' type='button' onclick='reject_company({})' value=添加驳回原因 >",obj.id)
        if not obj.user.is_staff:
            report = format_html("<input style='width:140px' type='button' onclick='verify_company({})' value=通过审核 >",obj.id)
        return report
    
    new_status.short_description = '状态'
    # class Media:        
    #     js = ('/static/js/balance.js',)

    def livenesssuper(self,obj):
        
        if obj.status == 10:
            return format_html("<input style='width:140px' type='button' onclick=window.location.href='/redeclare?cid={}' value=重新申请 >",obj.id)
        elif obj.status >= 1:
            return '较活跃'
        else:
            return '欠活跃'

    def liveness(self,obj):
        if obj.status >= 1:
            return '较活跃'
        else:
            return '欠活跃'

    liveness.short_description = '活跃度'
    livenesssuper.short_description = '活跃度'

    def business_license_pic_show(self,obj):

        path = str(obj.business_license_pic)
        if not path.startswith('static/'):
            path = 'static/' + path
        return format_html('<div style="height: 25px;overflow: hidden;"><a href="/' + path + '" width=30 height=50 data-lightbox="' + path + '"><img src="/' + path + '" width=30 height=50" /></a></div>')
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



@admin.register(PTOfEnterprises)
class PTOfEnterprisesAdmin(admin.ModelAdmin):
    readonly_fields = ('companyInfo',)
    search_fields = ('companyInfo__name',)
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if get_user_group(request,'super'):
            return qs.filter(companyInfo__user__id__gt=0)

    # def get_readonly_fields(self,request,obj):
    #     if obj and obj.companyInfo.status > 3:
    #         return ('companyInfo','external_environment','products_and_market','technology_R_D','team')
    #     return self.readonly_fields

    class Media:
        js = ('/static/js/opt_evaluation.js',)




        


@admin.register(IndependentEvaluationOfEnterprises)
class IndependentEvaluationOfEnterprisesAdmin(admin.ModelAdmin):
    list_display=['companyInfo','external_environment','products_and_market','technology_R_D','team','create_date']
    # exclude = ('companyInfo',)
    search_fields = ('companyInfo__name',)
    readonly_fields = ('companyInfo',)
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if get_user_group(request,'super'):
            return qs.filter(companyInfo__user__id__gt=0)
        elif get_user_group(request,'企业用户'):
            return qs.filter(companyInfo=CompanyInfo.objects.get(user=request.user))
        elif get_user_group(request,'孵化器用户'):
            return qs.filter(companyInfo__incubator=Incubator.objects.get(user=request.user),companyInfo__user__id__gt=0)

    def get_readonly_fields(self,request,obj):
        if obj and obj.companyInfo.status > 3:
            return ('companyInfo','external_environment','products_and_market','technology_R_D','team')
        return self.readonly_fields

    def get_list_display(self, request, obj=None):
        if  get_user_group(request,'孵化器用户'):
            return ['companyInfo','external_environment_add','products_and_market_add','technology_R_D_add','team_add','create_date']
        elif get_user_group(request,'super'):
            return ['companyInfo','external_environment_addpt','products_and_market_addpt','technology_R_D_addpt','team_addpt','create_date']
        return self.list_display


    def save_model(self, request, obj, form, change):
        obj.companyInfo = CompanyInfo.objects.get(user=request.user)
        obj.save()

        cobj = CompanyInfo.objects.get(user=request.user)
        if cobj.status == 2:
            cobj.status = 3
            cobj.save()
            if not CompanyStatus.objects.filter(companyInfo=cobj,status=3):
                CompanyStatus.objects.create(companyInfo=cobj,status=3)

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


    # def change_view(self, request, object_id, form_url='', extra_context=None):
    #     return self.changeform_view(request, object_id, form_url, extra_context)

    def external_environment_addpt(self,obj):
        eobjs = EvaluationOfEnterprises.objects.filter(companyInfo=obj.companyInfo)
        pobjs = PTOfEnterprises.objects.filter(companyInfo=obj.companyInfo)


        if eobjs and eobjs[0].external_environment:
            eda = '%s分' % eobjs[0].external_environment
        else:
            eda = '--'

        if pobjs and pobjs[0].external_environment:
            pda = '%s分' % pobjs[0].external_environment
        else:
            pda = '--'

        if obj.external_environment:
            ida = '%s分' % obj.external_environment
        else:
            ida = '--'
        return '%s （%s %s）' % (pda ,eda,ida)

    def products_and_market_addpt(self,obj):
        eobjs = EvaluationOfEnterprises.objects.filter(companyInfo=obj.companyInfo)
        pobjs = PTOfEnterprises.objects.filter(companyInfo=obj.companyInfo)


        if eobjs and eobjs[0].products_and_market:
            eda = '%s分' % eobjs[0].products_and_market
        else:
            eda = '--'

        if pobjs and pobjs[0].products_and_market:
            pda = '%s分' % pobjs[0].products_and_market
        else:
            pda = '--'

        if obj.products_and_market:
            ida = '%s分' % obj.products_and_market
        else:
            ida = '--'
        return '%s （%s %s）' % (pda ,eda,ida)

    def technology_R_D_addpt(self,obj):
        eobjs = EvaluationOfEnterprises.objects.filter(companyInfo=obj.companyInfo)
        pobjs = PTOfEnterprises.objects.filter(companyInfo=obj.companyInfo)


        if eobjs and eobjs[0].technology_R_D:
            eda = '%s分' % eobjs[0].technology_R_D
        else:
            eda = '--'

        if pobjs and pobjs[0].technology_R_D:
            pda = '%s分' % pobjs[0].technology_R_D
        else:
            pda = '--'

        if obj.technology_R_D:
            ida = '%s分' % obj.technology_R_D
        else:
            ida = '--'
        return '%s （%s %s）' % (pda ,eda,ida)

    def team_addpt(self,obj):
        eobjs = EvaluationOfEnterprises.objects.filter(companyInfo=obj.companyInfo)
        pobjs = PTOfEnterprises.objects.filter(companyInfo=obj.companyInfo)


        if eobjs and eobjs[0].team:
            eda = '%s分' % eobjs[0].team
        else:
            eda = '--'

        if pobjs and pobjs[0].team:
            pda = '%s分' % pobjs[0].team
        else:
            pda = '--'

        if obj.team:
            ida = '%s分' % obj.team
        else:
            ida = '--'
        return '%s （%s %s）' % (pda ,eda,ida)

    external_environment_add.short_description = '企业所处外部环境（企业自评）'
    products_and_market_add.short_description = '企业主营产品及市场开拓（企业自评）'
    technology_R_D_add.short_description = '企业核心技术及研发实力（企业自评）'
    team_add.short_description = '企业经营及管理团队（企业自评）'

    external_environment_addpt.short_description = '企业所处外部环境（校正评价 企业自评）'
    products_and_market_addpt.short_description = '企业主营产品及市场开拓（校正评价 企业自评）'
    technology_R_D_addpt.short_description = '企业核心技术及研发实力（校正评价 企业自评）'
    team_addpt.short_description = '企业经营及管理团队（校正评价 企业自评）'


    class Media:
        js = ('/static/js/opt_evaluation.js',)

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
        CompanyStatus.objects.create(companyInfo=obj.companyInfo,status=7)


    class Media:
        js = ('/static/js/opt_evaluation.js',)
# EvaluationOfEnterprises




@admin.register(RejectReason)
class RejectReasonAdmin(admin.ModelAdmin):
    list_display = ['companyInfo','text','is_alive','create_date']
    search_fields = ('companyInfo__name', 'text')
    list_editable = ('is_alive',)

    class Media:
        js = ('/static/js/debug_rejectreasonadmin.js',)

@admin.register(Balance)
class BalanceAdmin(admin.ModelAdmin):
    list_display = ['year']
    def get_queryset(self, request):
        qs = super().get_queryset(request)

        yearlist = Balance.objects.filter(companyInfo=CompanyInfo.objects.get(user=request.user)).values('year').annotate(yearNum=Count("year"))
        years = set()
        for yea in yearlist:
            years.add(yea['year'])

        bs = qs.filter(id=-133)
        for year in years:
            bl = Balance.objects.filter(year=year)[0].id
            bl = Balance.objects.filter(id=bl)
            # bs = qs | bl
            if not bs:
                bs = bl 
            else:
                bs |= bl

        return bs


@admin.register(Profit)
class ProfitAdmin(admin.ModelAdmin):
    list_display = ['year']
    def get_queryset(self, request):
        qs = super().get_queryset(request)

        yearlist = Profit.objects.filter(companyInfo=CompanyInfo.objects.get(user=request.user)).values('year').annotate(yearNum=Count("year"))

        years = set()
        for yea in yearlist:
            years.add(yea['year'])

        bs = qs.filter(id=-133)
        for year in years:
            bl = Profit.objects.filter(year=year)[0].id
            bl = Profit.objects.filter(id=bl)
            # bs = qs | bl
            if not bs:
                bs = bl 
            else:
                bs |= bl

        return bs

@admin.register(CashFlow)
class CashFlowAdmin(admin.ModelAdmin):
    list_display = ['year']
    def get_queryset(self, request):
        qs = super().get_queryset(request)

        yearlist = CashFlow.objects.filter(companyInfo=CompanyInfo.objects.get(user=request.user)).values('year').annotate(yearNum=Count("year"))
        years = set()
        for yea in yearlist:
            years.add(yea['year'])

        bs = qs.filter(id=-133)
        for year in years:
            bl = CashFlow.objects.filter(year=year)[0].id
            bl = CashFlow.objects.filter(id=bl)
            # bs = qs | bl
            if not bs:
                bs = bl 
            else:
                bs |= bl
        return bs



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
