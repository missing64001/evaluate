from django.contrib import admin
from .models import Incubator
from company.models import CompanyInfo

# Register your models here.
@admin.register(Incubator)
class IncubatorAdmin(admin.ModelAdmin):
    list_display = ['name','phone','company_amount']
    exclude = ['user']

    def company_amount(self,obj):
        return len(CompanyInfo.objects.all().filter(incubator=obj))
    company_amount.short_description = '企业数量'


    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)