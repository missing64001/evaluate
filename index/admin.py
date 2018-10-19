from django.contrib import admin
from .models import *
from company.models import CompanyInfo,get_user_group
from incubator.models import Incubator
from django.contrib.auth.models import User




admin.site.unregister(User)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','phone','email','group','owned_enterprise','owned_incubator','date_joined')
    
    def phone(self,user):
        companyInfo=CompanyInfo.objects.get(user=user)
        return str(companyInfo.phone)
    phone.short_description = '联系电话'
    
    def group(self,user):
        try:
            return user.groups.all()[0].name
        except Exception as e:
            return 'superuser'
    group.short_description = '账户类型'

    def owned_enterprise(self,user):
        if get_user_group(user,'企业用户'):
            return CompanyInfo.objects.get(user=user)
    owned_enterprise.short_description = '所属企业'

    def owned_incubator(self,user):

        if get_user_group(user,'企业用户'):

            return CompanyInfo.objects.get(user=user).incubator


        elif get_user_group(user,'孵化器用户'):
            return Incubator.objects.get(user=user)
    owned_incubator.short_description = '所属孵化器'

    # def expired(self, obj):
    #     """自定义列表字段, 根据数据单截止日期和当前日期判断是否过期,并对数据库进行更新"""
    #     import datetime
    #     from django.utils.html import format_html
    #     end_date = obj.end_date
    #     if end_date >= datetime.date.today():
    #         ret = '未过期'
    #         color_code = 'green'
    #     else:
    #         ret = '已过期'
    #         color_code = 'red'
    #     DataPaperStore.objects.filter(pk=obj.pk).update(is_expired=ret)
    #     return format_html(
    #                 '<span style="color: {};">{}</span>',
    #                 color_code,
    #                 ret,
    #             )
    # expired.short_description = '是否已过期'
    # 
    # 
    @admin.register(Bonus)
    class BonusAdmin(admin.ModelAdmin):
        list_display = ('companyInfo','incubator','item','note','value')
        search_fields = ('companyInfo__name','companyInfo__incubator__name')

        def incubator(self,obj):

            return obj.companyInfo.incubator
            
    @admin.register(Subtraction)
    class SubtractionAdmin(admin.ModelAdmin):
        list_display = ('companyInfo','incubator','item','note','value')
        search_fields = ('companyInfo__name','companyInfo__incubator__name')

        def incubator(self,obj):

            return obj.companyInfo.incubator








