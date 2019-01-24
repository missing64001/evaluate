from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse
from evaluateg import settings
from company.models import get_user_group
from institution.models import Institution
class m1(MiddlewareMixin):

    def process_request(self, request):
        if get_user_group(request,'super'):
            settings.SUIT_CONFIG['MENU'] = (
                'sites',

                {'label': '用户数据管理',
                  'app': 'incubator',
                  'models': (

                            {'label': '孵化器数据统计', 'model': 'Incubator'},

                            {'label': '企业数据统计', 'url': '/admin/company/companyinfo'},

                )},

                {'label': '评分管理',
                  'app': 'incubator',
                  'models': (

                             {'label': '平台评价', 'url': '/admin/company/independentevaluationofenterprises/'},

                            'index.Bonus','index.Subtraction',
                )},
                {'label': '报告管理',
                  'app': 'institution',
                  'models': (
                            {'label': '生成报告', 'url': '/admin/institution/report/'},
                            'InvestReport',
                            'BankReport',
                )},

                {'label': '账号管理',
                  'app': 'incubator',
                  'models': (

                            {'label': '账号管理', 'url': '/admin/auth/user/'},

                )},

                {'label': '反馈信息',
                  'app': 'institution',
                  'models': (

                            'institution.ReportBack',

                )},
                  
                # {'label': '基本信息',
                #   'app': 'company',
                #   'models': (
                #             {'label': '企业基本信息', 'url': '/admin/company/companyinfo'},
                #             {'label': '校正评价', 'model': 'IndependentEvaluationOfEnterprises'},
                #             # 'FinancialSituation','ProductsAndMarket','TechnologyRD','ServerRequest',
                #             'institution.ReportBack',

                # )},
             )
            
        elif get_user_group(request,'企业用户'):
            settings.SUIT_CONFIG['MENU'] = (
                {'label': '基本信息',
                  'app': 'company',
                  'models': (
                            # {'label': '企业基本信息', 'url': '/admin/company/companyinfo'},
                            'CompanyInfo',
                            # 'FinancialSituation','ProductsAndMarket','TechnologyRD','ServerRequest',

                )},


                {'label': '财务数据',
                  'app': 'company',
                  'models': (
                            {'label': '资产负债表', 'url': '/admin/company/balance'},
                            {'label': '利润表', 'url': '/admin/company/profit'},
                            {'label': '现金流量表', 'url': '/admin/company/cashflow'},
                )},

                {'label': '自主评价',
                  'app': 'company',
                  'models': (
                            'IndependentEvaluationOfEnterprises',
                )},

                {'label': '企业进度',
                  'app': 'company',
                  'models': (
                            {'label': '企业进度', 'url': '/admin/company/company_status/'},
                )},
                  

                {'label': '反馈信息',
                  'app': 'company',
                  'models': (
                            'institution.ReportBack',
                )},
             )
        elif get_user_group(request,'孵化器用户'):
            settings.SUIT_CONFIG['MENU'] = (

                  
                {'label': '孵化器',
                  'app': 'company',
                  'models': (
                            {'label': '企业基本信息', 'url': '/admin/company/companyinfo'},
                            {'label': '校正评价', 'model': 'IndependentEvaluationOfEnterprises'},
                            'RejectReason',
                            # 'FinancialSituation','ProductsAndMarket','TechnologyRD','ServerRequest',
                            'institution.ReportBack',

                )},
             )

        elif get_user_group(request,'机构用户'):


            _type = Institution.objects.get(user=request.user).type

            if _type == 1:
                report = 'institution.InvestReport'
            elif _type == 2:
                report = 'institution.BankReport'
            else:
                raise ValueError('错误的type类型:' + str(_type))
            settings.SUIT_CONFIG['MENU'] = (

                  
                {'label': '基本信息',
                  'app': 'institution',
                  'models': (
                            {'label': '金融报告 ', 'model': report},
                            'institution.ReportBack',

                )},
             )

    # def process_response(self, request, response):
    #     print(response)
    #     from pprint import pprint
    #     pprint(dir(response))
    #     return response

    # def process_exception(self, request, exception): 
    #     return HttpResponse("in exception")

