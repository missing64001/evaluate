


from django.contrib.auth.models import Group
from company.models import get_user_group


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





    return {
      'global_group': get_user_group(request),
      'global_url': global_url,
      # request.user.username,
    }
