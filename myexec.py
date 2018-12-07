





print(333)

cobj = CompanyInfo.objects.get(user=request.user)
status = cobj.status



status = 1



#设置 流程图
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
    status_text[0] = '企业提交信息'
    status_text[1] = '所属孵化器驳回企业信息'


if status < 4:
    status_pic[1] = '2'
    status_pic[0] = 'wait'

    status_text[1] = '孵化器进度未开始'
    status_text[0] = '企业提交信息'

    status_line[0] = '_grap'

if status == 2:
    status_text[0] = '企业进行自我评价'
if status == 1:
    status_text[0] = '企业上传财务报表'
if status == 0:
    status_text[0] = '企业填写企业信息'
if status in (3,5):
    showbutton = True
else:
    showbutton = False


if False:
    nodes = []
    nodes.append((0,request.user.date_joined,'企业填写企业信息　　下一步：上传企业财务报表'))
    cstatusall = CompanyStatus.objects.filter(companyInfo=cobj).order_by('id')
    cstatusall = [(s.status,s.create_date) for s in cstatusall]
    rreasons = RejectReason.objects.filter(companyInfo=cobj)
    rreasonlst = []
    for reason in rreasons:
        text = reason.text
        rreasonlst.append([text[:39]])
        text = text[39:]
        while len(text) > 0:
            rreasonlst[-1].append(text[:39])
            text = text[39:]


    for cstatus in cstatusall:
        status = cstatus.status
        create_date = cstatus.create_date
        if status == 1:
            nodes.append((status,create_date,'企业上传财务报表　　下一步：企业进行自我评价'))
        elif status == 2:
            nodes.append((status,create_date,'企业进行自我评价　　下一步：企业提交信息'))
        elif status == 3:
            nodes.append((status,create_date,'企业提交信息　　下一步：所属孵化器审核企业信息'))
        elif status == 4:
            nodes.append((status,create_date,'所属孵化器审核企业信息'))
        elif status == 5:
            nodes.append(rreasonlst)
            nodes.append((status,create_date,'所属孵化器驳回企业信息　　下一步：企业提交信息'))
        elif status == 7:
            nodes.append((status,create_date,'所属孵化器修正企业评价　　孵化器进度已完成　　下一步：平台发送评估报告到机构'))
        elif status == 8:
            nodes.append((status,create_date,'平台发送评估报告到机构　　平台进度已完成　　下一步：等待机构反馈给平台'))
        elif status == 9:
            nodes.append((status,create_date,'投资机构反馈给平台　　投资机构进度已完成　　下一步：等待平台发送反馈信息'))
        elif status == 10:
            nodes.append((status,create_date,'您已收到来自平台的反馈信息'))
            
else:
    nodes = []
    nodes.append((0,request.user.date_joined,'企业填写企业信息　　下一步：上传企业财务报表'))
    rreasons = ['士大夫大师傅广泛大概的轨道发射灌水灌水','广泛广泛还是感觉三股势力感觉广泛124广泛还14354654是感觉三股泛124广泛还是感觉三股泛124广泛还是感觉三股势力感觉广456泛广泛还是感觉三股势力感觉广泛456广泛还是感678觉三股势力感觉广泛广泛还是感觉三股势力感觉广泛广泛还是感觉三股势力感觉广泛广泛还是感觉三股势力感觉广泛广泛还是感觉三股势力感觉广泛广泛还是感觉三股势力感觉广泛广泛还是感觉三股势力感觉',

                '广泛广泛还是感觉三股势力感觉','广泛广泛还是感觉三股势力感觉广泛广泛还是感觉三股势力感觉广泛广泛还是感觉三股势力感觉','广泛广泛还是感觉三股势力感觉']
    rreasonlst = []
    for reason in rreasons:
        text = reason
        rreasonlst.append([text[:39]])
        text = text[39:]
        while len(text) > 0:
            rreasonlst[-1].append(text[:39])
            text = text[39:]

    pprint(rreasonlst)
    for cstatus in range(10):
        status = cstatus
        create_date = '2018-12-11 15:34:13'
        if status == 1:
            nodes.append((status,create_date,'企业上传财务报表　　下一步：企业进行自我评价'))
        elif status == 2:
            nodes.append((status,create_date,'企业进行自我评价　　下一步：企业提交信息'))
        elif status == 3:
            nodes.append((status,create_date,'企业提交信息　　下一步：所属孵化器审核企业信息'))
        elif status == 4:
            nodes.append((status,create_date,'所属孵化器审核企业信息'))
        elif status == 5:
            nodes.append(rreasonlst)
            nodes.append((status,create_date,'所属孵化器驳回企业信息　　下一步：企业提交信息'))
            # 添加驳回原因
        elif status == 7:
            nodes.append((status,create_date,'所属孵化器修正企业评价　　孵化器进度已完成　　下一步：平台发送评估报告到机构'))
        elif status == 8:
            nodes.append((status,create_date,'平台发送评估报告到机构　　平台进度已完成　　下一步：等待机构反馈给平台'))
        elif status == 9:
            nodes.append((status,create_date,'投资机构反馈给平台　　投资机构进度已完成　　下一步：等待平台发送反馈信息'))
        elif status == 10:
            nodes.append((status,create_date,'您已收到来自平台的反馈信息'))
            






x = '驳回原因：驳回原因：驳回原因：驳回原因：驳回原驳回原因：驳回原驳回原因：驳回原'
print(len(x))







global res
res = render(request,'company_status.html',{'nodes':reversed(nodes),'showbutton':showbutton,'status_pic':status_pic,'status_text':status_text,'status_line':status_line})