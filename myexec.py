







cobj = CompanyInfo.objects.get(user=request.user)
status = cobj.status



status = 10

status_pic = ['finished','finished','finished','finished','finished']
status_text = ['企业进度已完成','孵化器进度已完成','平台进度已完成','投资机构进度已完成','企业收到反馈信息']
status_line = [''] * 4

if status < 10:
    status_pic[4] = 'wait'
    status_text[4] = '等待平台发送反馈信息'
if status < 9:
    status_pic[4] = '5'
    status_pic[3] = 'wait'

    status_text[4] = '企业未收到反馈信息'
    status_text[3] = '等待投资机构反馈给平台'

    status_line[3] = '_grap'
if status < 8:
    status_pic[3] = '4'
    status_pic[2] = 'wait'

    status_text[3] = '投资机构进度未开始'
    status_text[2] = '平台发送评估报告到机构'

    status_line[2] = '_grap'
if status < 7:
    status_pic[2] = '3'
    status_pic[1] = 'wait'

    status_text[2] = '平台进度未开始'
    status_text[1] = '所属孵化器审核企业信息'

    status_line[1] = '_grap'
if status == 5:


    status_pic[0] = 'wait'
    status_text[0] = '等待企业提交信息'
    status_text[1] = '所属孵化器驳回企业信息'


if status < 4:
    status_pic[1] = '2'
    status_pic[0] = 'wait'

    status_text[1] = '孵化器进度未开始'
    status_text[0] = '等待企业提交信息'

    status_line[0] = '_grap'

if status == 2:
    status_text[0] = '企业进行自我评价'
if status == 1:
    status_text[0] = '企业上传财务报表'
if status == 0:
    status_text[0] = '企业填写企业信息'


print(status,status_pic)
global res
res = render(request,'company_status.html',{'status_pic':status_pic,'status_text':status_text,'status_line':status_line})