from django.contrib import admin
from .models import Incubator
from company.models import CompanyInfo

# Register your models here.
@admin.register(Incubator)
class IncubatorAdmin(admin.ModelAdmin):
    list_display = ['name','phone','credit_code','company_amount']
    exclude = ['user']

    def company_amount(self,obj):
        return len(CompanyInfo.objects.all().filter(incubator=obj))
    company_amount.short_description = '企业数量'


