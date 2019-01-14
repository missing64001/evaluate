


from django.contrib.auth.models import Group
from company.models import get_user_group,CompanyInfo
from institution.models import BankReport,InvestReport
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
    # print(request.path)

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



    data = {
      'global_group': get_user_group(request),
      'global_url': global_url,
      'global_is_close_save':global_is_close_save,
      # request.user.username,
    }



    #添加报告的全局数据
    if get_user_group(request,'super') or get_user_group(request,'机构用户'):
        report_data = []
        bobj = None
        url = r'/admin/institution/bankreport/(\d+)/change/'
        res = re.findall(url,request.path)
        if res:
            # print('匹配')
            bobj = BankReport.objects.get(id=int(res[0]))
            report_items = (
                '评分要点',
                '外部环境（20）',
                '企业主营产品及市场开拓（20）',
                '企业核心技术及研发实力（20）',
                '企业经营及管理团队（40）',
                '应收账款周转率（5）',
                '存货周转率（5）',
                '总资产周转率（5）',
                '净利润增长率（10）',
                '净资产增长率（5）',
                '销售收入增长率（5）',
                '*净利润率（10）',
                '总资产报酬率（5）',
                '*净资产收益率（5）',
                '*资产负债率（10）',
                '*经营现金流量负债比（10）',
                '*流动比率（7）',
                '*利息保障倍数（8）',
                '研发费用收入比例（10）',
                )
            fenzhi = (5,5,5,10,5,5,10,5,5,10,10,7,8,10)


        url = r'/admin/institution/investreport/(\d+)/change/'
        res = re.findall(url,request.path)
        if not res:
            res = re.findall(url,request.path)
        if res:
            # print('匹配')
            bobj = InvestReport.objects.get(id=int(res[0]))
            report_items = (
                '评分要点',
                '外部环境（20）',
                '企业主营产品及市场开拓（20）',
                '企业核心技术及研发实力（20）',
                '企业经营及管理团队（40）',
                '应收账款周转率（10）',
                '存货周转率（7）',
                '总资产周转率（8）',
                '净利润增长率（10）',
                '净资产增长率（5）',
                '销售收入增长率（10）',
                '*净利润率（10）',
                '总资产报酬率（5）',
                '*净资产收益率（5）',
                '*资产负债率（5）',
                '*经营现金流量负债比（5）',
                '*流动比率（5）',
                '*利息保障倍数（5）',
                '研发费用收入比例(10)',
                )
            fenzhi = (10,7,8,10,5,10,10,5,5,5,5,5,5,10)
            

        if bobj:
            years = [report_items[0] ]+ [ str(y) + '年'  for y in bobj.years.split('_')]
            report_data.append(years)
            for i in range(1,5):
                x = getattr(bobj,'i%s'%i)
                report_data.append( [report_items[i] ] + ['%s分' % x] + [ '' ] * (len(years)-2))

            for i in range(5,19):
                x = getattr(bobj,'i%s'%i)
                report_data.append( [report_items[i] ] + [ int(s) for s in x])

            for i in range(5,19):
                for j in range(1,len(report_data[i])):
                    report_data[i][j] = report_data[i][j] * fenzhi[i-5]

            def getdata_data(j,i):
                i = int(i[1:])
                return report_data[i][j]
            fin_totle = ['财务报表总得分']
            for j in range(1,len(years)):
                fin = (
                    getdata_data(j,'i5') +getdata_data(j,'i6') +getdata_data(j,'i7') +getdata_data(j,'i8') +getdata_data(j,'i9') +getdata_data(j,'i10') +
                    getdata_data(j,'i11') +getdata_data(j,'i12') +getdata_data(j,'i13') +getdata_data(j,'i14') +getdata_data(j,'i15') +getdata_data(j,'i16') +
                    getdata_data(j,'i17') +getdata_data(j,'i18')) * 0.65
                fin_totle.append('%s分' % fin)

            for i in range(5,19):
                for j in range(1,len(report_data[i])):
                    report_data[i][j] = str(report_data[i][j]) + '分'


            bonus = (['加分'] + ['%s分' % bobj.bonus] + [ '' ] * (len(years)-2))
            subtraction = (['减分'] + ['%s分' % bobj.subtraction] + [ '' ] * (len(years)-2))
            totle = (['总分'] + ['%s分' % bobj.totle] + [ '' ] * (len(years)-2))

            report_data += [fin_totle,bonus,subtraction,totle]


            data['report_data'] = report_data


        if get_user_group(request,'super') and request.path in ('/admin/index/bonus/','/admin/index/subtraction/'):
            
            data['global_is_action'] = 'global_is_action'
            

            # res = re.search(url,request.path)
            # if res







    return data


