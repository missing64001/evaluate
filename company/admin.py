from django.contrib import admin
from .models import *

class ShareholderInl(admin.StackedInline):
    model = Shareholder
    extra = 1
    max_num = 5
    readonly_fields = ('name','share_ratio','form_of_contribution')

class EnterpriseAwardsInl(admin.StackedInline):
    model = EnterpriseAwards
    extra = 0
    max_num = 5

class PersonalAwardsInl(admin.StackedInline):
    model = PersonalAwards
    extra = 0
    max_num = 5

class ProjectInl(admin.StackedInline):
    model = Project
    extra = 0
    max_num = 5
    
class PatentInl(admin.StackedInline):
    model = Patent
    extra = 0
    max_num = 5
    
class DrugApprovalInl(admin.StackedInline):
    model = DrugApproval
    extra = 0
    max_num = 5    

class MIRCInl(admin.StackedInline):
    model = MIRC
    extra = 0
    max_num = 5    

class StandardSettingInl(admin.StackedInline):
    model = StandardSetting
    extra = 0
    max_num = 5

class CoreMemberInl(admin.StackedInline):
    model = CoreMember
    extra = 1
    max_num = 5

class EducationExperienceInl(admin.StackedInline):
    model = EducationExperience
    extra = 1
    max_num = 5

class WorkExperienceInl(admin.StackedInline):
    model = WorkExperience
    extra = 1
    max_num = 5


class FinancialSituationInl(admin.StackedInline):
    model = FinancialSituation
    extra = 1
    max_num = 5
class ProductsAndMarketInl(admin.StackedInline):
    model = ProductsAndMarket
    extra = 1
    # max_num = 5
class TechnologyRDInl(admin.StackedInline):
    model = TechnologyRD
    extra = 1
    # max_num = 5
class ServerRequestInl(admin.StackedInline):
    model = ServerRequest
    extra = 1
    # max_num = 5
    

    
@admin.register(IndependentEvaluationOfEnterprises)
class IndependentEvaluationOfEnterprisesAdmin(admin.ModelAdmin):
    exclude = ('companyInfo',)
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(companyInfo=CompanyInfo.objects.get(user=request.user))

    class Media:
        js = ('/static/js/opt_evaluation.js',)

    def save_model(self, request, obj, form, change):
        obj.companyInfo = CompanyInfo.objects.get(user=request.user)
        obj.save()

@admin.register(CoreMember)
class CoreMemberAdmin(admin.ModelAdmin):
    inlines = [EducationExperienceInl,WorkExperienceInl]
    exclude = ('companyInfo',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(companyInfo=CompanyInfo.objects.get(user=request.user))

@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display=['name','phone','incubator','credit_code']
    search_fields = ('name','incubator__name')
    inlines = [ShareholderInl, EnterpriseAwardsInl,PersonalAwardsInl,ProjectInl,PatentInl,
                DrugApprovalInl,MIRCInl,StandardSettingInl,] #CoreMemberInl,
    exclude = ('user',)



    def get_inline_instances(self, request, obj=None):
        inline_instances = []
        if request.user.groups.all()[0].name == '孵化器用户':
            inlines = self.inlines + [FinancialSituationInl,ProductsAndMarketInl,TechnologyRDInl,ServerRequestInl]
        else:
            inlines = self.inlines

        for inline_class in inlines:
            inline = inline_class(self.model, self.admin_site)
            if request:
                if not (inline.has_add_permission(request) or
                        inline.has_change_permission(request, obj) or
                        inline.has_delete_permission(request, obj)):
                    continue
                if not inline.has_add_permission(request):
                    inline.max_num = 0
            inline_instances.append(inline)

        return inline_instances


    # def get_inline_instances(self, request,obj=None):
    #     inlines = [ShareholderInl, EnterpriseAwardsInl,PersonalAwardsInl,ProjectInl,PatentInl,
    #             DrugApprovalInl,MIRCInl,StandardSettingInl,

    #     return inlines

    def get_readonly_fields(self, request,obj=None):
        if request.user.groups.all()[0].name == '孵化器用户':
            return ('user','incubator','name','create_date','registered_capital','paid_in_capital',
                'major_business','work_force','junior_college_number','developer_number','is_high_tech_enterprise'
                ,'abouts','field_1','field_2','technical_source')
        return []

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        elif request.user.groups.all()[0].name == '孵化器用户':

            return qs.filter(incubator=Incubator.objects.get(user=request.user))
        return qs.filter(user=request.user)

    # class Media:        
    #     js = ('/static/js/balance.js',)





    
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
