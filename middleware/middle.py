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

                {'label': '平台管理团队',
                  'app': 'incubator',
                  'models': (

                            {'label': '用户管理', 'url': '/admin/auth/user/'},

                            'Incubator','index.Bonus','index.Subtraction',

                            {'label': '企业评估报告', 'url': '/admin/institution/report'},
                            'institution.ReportBack',
                )},

                  
                # {'label': '基本信息',
                #   'app': 'company',
                #   'models': (
                #             {'label': '企业基本信息', 'url': '/admin/company/companyinfo_opt'},
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
                            {'label': '企业基本信息', 'url': '/admin/company/companyinfo_opt'},
                            'IndependentEvaluationOfEnterprises',
                            # 'FinancialSituation','ProductsAndMarket','TechnologyRD','ServerRequest',
                            {'label': '资产负债表', 'url': '/admin/company/balance'},
                            {'label': '利润表', 'url': '/admin/company/profit'},
                            {'label': '现金流量表', 'url': '/admin/company/cash_flow'},
                            'institution.ReportBack',

                )},
             )
        elif get_user_group(request,'孵化器用户'):
            settings.SUIT_CONFIG['MENU'] = (

                  
                {'label': '基本信息',
                  'app': 'company',
                  'models': (
                            {'label': '企业基本信息', 'url': '/admin/company/companyinfo_opt'},
                            {'label': '校正评价', 'model': 'IndependentEvaluationOfEnterprises'},
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
                  'app': 'company',
                  'models': (
                            # {'label': '企业基本信息', 'url': '/admin/company/companyinfo_opt'},
                            report,
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

