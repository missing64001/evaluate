from django.contrib import admin
from .models import *
from company.models import *
from index.models import Bonus,Subtraction
from django.utils.html import format_html

# Register your models here.


@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    fields = ['type','name','phone']
    readonly_fields = ('type','name')
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if get_user_group(request,'机构用户'):
            return qs.filter(user=request.user)

@admin.register(InvestReport)
class InvestReportAdmin(admin.ModelAdmin):
    readonly_fields = ('companyInfo',)
    fields = ('institution','companyInfo')
    list_display=['companyInfo','totle','create_date']
    search_fields = ('companyInfo__name',)


    def get_list_display(self, request, obj=None):
        if get_user_group(request,'super'):
            return ['companyInfo','totle','create_date','aopt']
        return self.list_display


    def aopt(self,obj):
        return format_html("""<input style='width:90px'  type='button' onclick='location.href=("/admin/institution/investreport/{}/change/")' value=发送报告 >"""
                ,obj.id)
    aopt.short_description = '操作'


    def get_user_group_1(self,obj):
        return format_html('''<span class="get_user_group">机构用户</span> <script type="text/javascript" src="/static/js/set_head.js"></script>''')
    


    def get_fields(self, request, obj=None):
        if get_user_group(request,'机构用户'):
            return ('companyInfo','get_user_group_1')
        else:
            return self.fields

    def get_readonly_fields(self, request,obj=None):
        if get_user_group(request,'机构用户'):
            return list(self.readonly_fields) + ['get_user_group_1']
        return self.readonly_fields

    def get_exclude(self, request, obj=None):

        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return self.exclude
        elif get_user_group(request,'机构用户'):
            return ('institution',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        elif get_user_group(request,'孵化器用户'):
            return
        elif get_user_group(request,'机构用户'):
            return qs.filter(institution__user=request.user)
        # return qs.filter(user=request.user)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "institution":
            kwargs["queryset"] = Institution.objects.filter(type=1)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def save_model(self, request, obj, form, change):
        cobj = CompanyInfo.objects.get(name=obj.companyInfo.name,user__id__gt=0) 
        cobj.status = 8
        cobj.save()
        obj.save()
        CompanyStatus.objects.create(companyInfo=cobj,status=8)


@admin.register(BankReport)
class BankReportAdmin(admin.ModelAdmin):
    readonly_fields = ('companyInfo',)
    fields = ('institution','companyInfo')
    list_display=['companyInfo','totle','create_date']
    search_fields = ('companyInfo__name',)


    def get_list_display(self, request, obj=None):
        if get_user_group(request,'super'):
            return ['companyInfo','totle','create_date','aopt']
        return self.list_display
    def aopt(self,obj):
        return format_html("""<input style='width:90px'  type='button' onclick='location.href=("/admin/institution/bankreport/{}/change/")' value=发送报告 >"""
                ,obj.id)
    aopt.short_description = '操作'
    
    def get_user_group_1(self,obj):
        return format_html('''<span class="get_user_group">机构用户</span> <script type="text/javascript" src="/static/js/set_head.js"></script>''')
    
    def get_fields(self, request, obj=None):
        if get_user_group(request,'机构用户'):
            return ('companyInfo','get_user_group_1')
        else:
            return self.fields
            
    def get_readonly_fields(self, request,obj=None):
        if get_user_group(request,'机构用户'):
            return list(self.readonly_fields) + ['get_user_group_1']
        return self.readonly_fields

    def get_exclude(self, request, obj=None):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return self.exclude
        elif get_user_group(request,'机构用户'):
            return ('institution',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        elif get_user_group(request,'孵化器用户'):
            return
        elif get_user_group(request,'机构用户'):
            return qs.filter(institution__user=request.user)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "institution":
            kwargs["queryset"] = Institution.objects.filter(type=2)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def save_model(self, request, obj, form, change):
        cobj = CompanyInfo.objects.get(name=obj.companyInfo.name,user__id__gt=0) 
        cobj.status = 8
        cobj.save()
        obj.save()
        CompanyStatus.objects.create(companyInfo=cobj,status=8)

class CompanyInfoReportAdmin(admin.ModelAdmin):
    list_display=['name','incubator','invest_report','bank_report']
    # list_editable = ['status']
    
    def get_queryset(self, request):
        # self.myrequest = request
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs.filter(user__id__gt=0)

        elif get_user_group(request,'机构用户'):
            return qs.filter(investreport__institution__user=request.user)

        return None

    def i_evaluate_status(self,obj,ishtml=True):
        try:
            iobj = IndependentEvaluationOfEnterprises.objects.get(companyInfo=obj)
            if iobj.external_environment and iobj.products_and_market and iobj.technology_R_D and iobj.team:
                eobj = EvaluationOfEnterprises.objects.get(companyInfo=obj)
                if eobj.external_environment and eobj.products_and_market and eobj.technology_R_D and eobj.team:
                    return format_html('<span style="color: {};">{}</span>','blue','已完成',) if ishtml else True
                else:
                    return format_html('<span style="color: {};">{}</span>','red','未校正',) if ishtml else False

            else:
                return format_html('<span style="color: {};">{}</span>','red','未完成',) if ishtml else False
        except IndependentEvaluationOfEnterprises.DoesNotExist:
            return format_html('<span style="color: {};">{}</span>','red','未完成',) if ishtml else False
        except EvaluationOfEnterprises.DoesNotExist:
            return format_html('<span style="color: {};">{}</span>','red','未校正',) if ishtml else False
            # format_html('<a href="/admin/company/independentevaluationofenterprises/%s">未校正评价</a>' % obj.id)
    i_evaluate_status.short_description = '自评状态'

    def balance_status(self,obj,ishtml=True):
        if len(Balance.objects.all().filter(companyInfo=obj)) > 0:
            return format_html('<span style="color: {};">{}</span>','blue','已完成',) if ishtml else True
        else:
            return format_html('<span style="color: {};">{}</span>','red','未完成',) if ishtml else False

    balance_status.short_description = '资产负债表'

    def profit_status(self,obj,ishtml=True):
        if len(Profit.objects.all().filter(companyInfo=obj)) > 0:
            return format_html('<span style="color: {};">{}</span>','blue','已完成',) if ishtml else True
        else:
            return format_html('<span style="color: {};">{}</span>','red','未完成',) if ishtml else False
    profit_status.short_description = '利润表'

    def cash_flow_status(self,obj,ishtml=True):
        if len(CashFlow.objects.all().filter(companyInfo=obj)) > 0:
            return format_html('<span style="color: {};">{}</span>','blue','已完成',) if ishtml else True
        else:
            return format_html('<span style="color: {};">{}</span>','red','未完成',) if ishtml else False
    cash_flow_status.short_description = '现金流量表'

    def invest_report(self,obj):
        if self.i_evaluate_status(obj,False) and self.balance_status(obj,ishtml=False) and \
        self.profit_status(obj,ishtml=False) and self.cash_flow_status(obj,ishtml=False):

            # request = self.myrequest
            Iobjs = InvestReport.objects.all().filter(companyInfo=obj) #,institution__user=request.user
            reportstr = ''
            for iobj in Iobjs:
                reportstr += '<option value="%s">%s</option>' % (iobj.id,(iobj.create_date+ timedelta(hours=8)).strftime("%Y-%m-%d"))

            # if get_user_group(request,'机构用户'):
            #     return format_html('''
            #     <select class="ms" type={} style="width:100px;">
            #         <option>查看</option>
            #         %s
            #     </select>
            #     '''%reportstr,0)

            return format_html("<input style='width:90px' cid={} _type=0 type='button' onclick='createcompanyreport(this)' value=生成报告 >"
                ,obj.id,obj.id)
    invest_report.short_description = '生成投资类报告'

    def bank_report(self,obj):
        if self.i_evaluate_status(obj,False) and self.balance_status(obj,ishtml=False) and \
        self.profit_status(obj,ishtml=False) and self.cash_flow_status(obj,ishtml=False):
            Bobjs = BankReport.objects.all().filter(companyInfo=obj)
            reportstr = ''
            for bobj in Bobjs:
                bobj
                reportstr += '<option value="%s">%s</option>' % (bobj.id,(bobj.create_date+ timedelta(hours=8)).strftime("%Y-%m-%d"))


            return format_html("<input style='width:90px' cid={} _type=1 type='button' onclick='createcompanyreport(this)' value=生成报告 >"
                ,obj.id,obj.id)
    bank_report.short_description = '生成银行类报告'
    class Media:
        js = ('/static/js/companyinforeportadmin.js',)





@admin.register(ReportBack)
class ReportBackAdmin(admin.ModelAdmin):
    exclude = ['investreport','bankreport',]
    search_fields = ('institution__name',)

    def get_list_display(self, request, obj=None):
        if get_user_group(request,'super'):
            return ['institution','mget_company','will','type','iscompanyview','isinstitutionview']
        else:
            return ['institution','mget_company','will','type']


    def get_exclude(self, request, obj=None):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return ['will'] + self.exclude

        elif get_user_group(request,'孵化器用户'):
            exclude = ['will','type','iscompanyview','isinstitutionview'] + self.exclude
            return exclude

        elif get_user_group(request,'企业用户'):
            exclude = ['will','type','iscompanyview','isinstitutionview'] + self.exclude
            return exclude

        elif get_user_group(request,'机构用户'):
            exclude = ['institution','iscompanyview','isinstitutionview'] + self.exclude
            return exclude

    def save_model(self, request, obj, form, change):


        if get_user_group(request,'机构用户'):
            obj.institution = Institution.objects.get(user=request.user)
            if 'report_id' in request.POST:
                _id = request.POST['report_id']
                if request.POST['report_type'] == 'investreport':
                    obj.investreport = InvestReport.objects.get(id=_id)
                elif request.POST['report_type'] == 'bankreport':
                    obj.bankreport = BankReport.objects.get(id=_id)
                else:
                    raise ValueError('错误的数据')
        obj.save()
        robj = obj.investreport or obj.bankreport
        if obj.iscompanyview == 2:
            cobj = CompanyInfo.objects.get(name=robj.companyInfo.name,user__id__gt=0) 
            cobj.status = 10
            cobj.save()
            CompanyStatus.objects.create(companyInfo=cobj,status=10)


    def get_readonly_fields(self, request,obj=None):
        if get_user_group(request,'super'):
            return ['institution','type','mget_company','mget_incubator','note']
        elif get_user_group(request,'孵化器用户'):
            return ['institution','mget_company','note']
        elif get_user_group(request,'企业用户'):
            return ['institution','note']
        # elif get_user_group(request,'机构用户'):
        #     return ['institution']
        return self.readonly_fields
        
    # def get_fieldsets(self, request, obj=None):
    #     # from pprint import pprint
    #     # pprint(dir(obj))
    #     if get_user_group(request,'机构用户'):
    #         return ((None,{'fields':('username','password','email','last_name','is_staff','is_active','groups')}),)
    #     return self.fieldsets

    def mget_company(self,obj):
        report = obj.investreport or obj.bankreport
        return report.companyInfo
    mget_company.short_description = '企业'

    def mget_incubator(self,obj):
        report = obj.investreport or obj.bankreport
        return report.companyInfo.incubator
    mget_incubator.short_description = '孵化器'


    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs

        elif get_user_group(request,'机构用户'):
            return qs.filter(institution__user=request.user)

        elif get_user_group(request,'孵化器用户'):
            return qs.filter(investreport__companyInfo__incubator__user=request.user,isinstitutionview=2) | qs.filter(bankreport__companyInfo__incubator__user=request.user,isinstitutionview=2)

        elif get_user_group(request,'企业用户'):
            return qs.filter(investreport__companyInfo__user=request.user,iscompanyview=2) | qs.filter(bankreport__companyInfo__user=request.user,iscompanyview=2)


    class Media:
        js = ('/static/js/debug_reportbackadmin.js',)