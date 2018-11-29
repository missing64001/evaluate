


from django.contrib.auth.models import Group
from company.models import get_user_group,CompanyInfo
import re

def globar_var(request):
    global_url = []
    is_show_save_button = False
    if get_user_group(request,'企业用户'):
        global_url = (
            '/admin/company/balance/',
            '/admin/company/profit/',
            '/admin/company/cashflow/',
            )
        
    elif get_user_group(request,'super'):
        global_url = (
            '/admin/index/bonus/',
            '/admin/index/subtraction/',
            '/admin/company/cashflow/',
            )
    elif get_user_group(request,'孵化器用户'):
        pass
    print(request.path)

    # global_is_close_save = 0





    # print('run_exec_test')
    # filename = 'myexec.py'
    # import traceback
    # try:
    #     with open(filename,'r',encoding='utf-8') as f:
    #         data = f.read()
    #     exec(data)
    # except Exception:
    #     traceback.print_exc()





    # 设置修改文件的保存按钮
    urls = []
    urls_super = [r'/admin/company/companyinfo/\d+/change/',
                  r'/admin/company/independentevaluationofenterprises/\d+/change/',
        ]
    urls_company_f = [r'/admin/company/companyinfo/\d+/change/',
                  r'/admin/company/independentevaluationofenterprises/\d+/change/',
                  r'/admin/institution/reportback/\d+/change/'
    ]
    urls_company = [
                  r'/admin/institution/reportback/\d+/change/',
    ]

    urls_fhq = [
                  r'/admin/company/companyinfo/\d+/change/',
                  r'/admin/institution/reportback/\d+/change/',
    ]
        
    if get_user_group(request,'super'):
        urls = urls_super

    elif get_user_group(request,'企业用户'):
        status = CompanyInfo.objects.get(user=request.user).status
        if status == 4 or status > 5:
            # print(1111)
            urls = urls_company_f
        else:
            urls = urls_company
    elif get_user_group(request,'孵化器用户'):
        urls = urls_fhq

    global_is_close_save = 0
    for url in urls:
        res = re.search(url,request.path)
        if res:
            # print('匹配')
            global_is_close_save = 1
            break






    return {
      'global_group': get_user_group(request),
      'global_url': global_url,
      'global_is_close_save':global_is_close_save,
      # request.user.username,
    }
