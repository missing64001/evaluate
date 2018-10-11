from django.contrib import admin
from .models import *

class ShareholderInl(admin.StackedInline):
    model = Shareholder
    extra = 1
    max_num = 5

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



@admin.register(CoreMember)
class CoreMemberInlAdmin(admin.ModelAdmin):
    inlines = [EducationExperienceInl,WorkExperienceInl]
    exclude = ('companyInfo',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(companyInfo=CompanyInfo.objects.get(user=request.user))

@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display=['name','create_date','registered_capital']
    inlines = [ShareholderInl, EnterpriseAwardsInl,PersonalAwardsInl,ProjectInl,PatentInl,
                DrugApprovalInl,MIRCInl,StandardSettingInl,] #CoreMemberInl,
    exclude = ('user',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)



    
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
