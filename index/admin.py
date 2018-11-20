from django.contrib import admin
from .models import *
from company.models import CompanyInfo,get_user_group
from incubator.models import Incubator
from institution.models import Institution

from django.contrib.auth.models import User,Group
from django.views.decorators.cache import never_cache

class IncubatorInl(admin.StackedInline):
    model = Incubator

class InstitutionInl(admin.StackedInline):
    model = Institution


    # extra = 0
    # max_num = 5
    # def get_readonly_fields(self, request,obj=None):
    #     if get_user_group(request,'企业用户'):
    #         return []
    #     return ('level','title','date')






# class MyAdminSite(admin.AdminSite):
#     @never_cache
#     def index(self, request, extra_context=None):
#         """
#         Displays the main admin index page, which lists all of the installed
#         apps that have been registered in this site.
#         """
#         app_list = self.get_app_list(request)

#         context = dict(
#             self.each_context(request),
#             title=self.index_title,
#             app_list=app_list,
#             xxxx= 'xxxx'
#         )
#         context.update(extra_context or {})

#         request.current_app = self.name

#         return TemplateResponse(request, self.index_template or 'admin/index.html', context)



admin.site.unregister(User)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','phone','email','group','owned_enterprise','owned_incubator','date_joined','is_staff')
    fields = ('username','email','is_staff','is_active','groups')
    inlines = [IncubatorInl,InstitutionInl]
    # readonly_fields = ('groups',)

    def get_inline_instances(self, request, obj=None):
        if request.GET.get('type'):
            type = request.GET['type']
        elif obj.groups:
            type = str(obj.groups.values('id')[0]['id'])

        if type == '2':
            return [inline(self.model, self.admin_site) for inline in self.inlines[0:1]]

        elif type == '3':
            return [inline(self.model, self.admin_site) for inline in self.inlines[1:]]

        return []

    def phone(self,user):
        if get_user_group(user,'企业用户'):
            obj=CompanyInfo.objects.get(user=user)
        elif get_user_group(user,'孵化器用户'):
            obj=Incubator.objects.get(user=user)
        elif get_user_group(user,'机构用户'):
            obj=Institution.objects.get(user=user)
            
        return str(obj.phone)
    phone.short_description = '联系电话'
    
    def group(self,user):
        try:
            gr = user.groups.all()[0].name
            if gr == '机构用户':
                if Institution.objects.get(user=user).type == 1:
                    return '投资机构用户'
                else:
                    return '金融机构用户'
            else:
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


    def formfield_for_dbfield(self, db_field, request, **kwargs):

        if request.GET.get('type'):
            type = request.GET['type']
        else:
            id = request.path.split('/')[-3]
            type = User.objects.get(id=id).groups.values('id')[0]['id']
        if db_field.name == 'groups':
            kwargs["queryset"] = Group.objects.filter(id= type)
        field =  super().formfield_for_dbfield(db_field, request, **kwargs)

        if db_field.name == 'is_staff':
            field.initial = True

        if db_field.name == 'groups':
            field.initial = type

        return field

    # def formfield_for_manytomany(self, db_field, request, **kwargs):
    #     if db_field.name == 'groups':
    #         kwargs["queryset"] = Group.objects.filter(id= request.GET['type'])
    #     field =  super().formfield_for_manytomany(db_field, request, **kwargs)
    #     if db_field.name == 'groups':
    #         field.initial = request.GET['type']
    #     return field



    # def save_model(self, request, obj, form, change):
    #     obj.user = request.user
    #     obj.save()


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
        incubator.short_description = '机构'
    @admin.register(Subtraction)
    class SubtractionAdmin(admin.ModelAdmin):
        list_display = ('companyInfo','incubator','item','note','value')
        search_fields = ('companyInfo__name','companyInfo__incubator__name')

        def incubator(self,obj):

            return obj.companyInfo.incubator
        incubator.short_description = '机构'



        def save_model(self, request, obj, form, change):
            obj.value = -abs(obj.value)
            obj.save()



