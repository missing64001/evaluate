# print(111)
# from company.models import CompanyInfo




# global global_is_close_save
# import re
# urls = []
# urls_super = [r'/admin/company/companyinfo/\d+/change/',
#               r'/admin/company/independentevaluationofenterprises/\d+/change/',
#     ]
# urls_company_f = [r'/admin/company/companyinfo/\d+/change/',
#               r'/admin/company/independentevaluationofenterprises/\d+/change/',
#               r'/admin/institution/reportback/\d+/change/'
# ]
# urls_company = [
#               r'/admin/institution/reportback/\d+/change/',
# ]

# urls_fhq = [
#               r'/admin/company/companyinfo/\d+/change/',
#               r'/admin/institution/reportback/\d+/change/',
# ]
    
# if get_user_group(request,'super'):
#     urls = urls_super

# elif get_user_group(request,'企业用户'):
#     status = CompanyInfo.objects.get(user=request.user).status
#     if status == 4 or status > 5:
#         print(1111)
#         urls = urls_company_f
#     else:
#         urls = urls_company
# elif get_user_group(request,'孵化器用户'):
#     urls = urls_fhq

# global_is_close_save = 0
# for url in urls:
#     res = re.search(url,request.path)
#     if res:
#         print('匹配')
#         global_is_close_save = 1
#         break