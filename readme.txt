


company 企业相关
    static
        css
            bootstrap.min.css 
                修改字体大小 12px 改为了 14px
            balance.css
                财务报表的样式

        js
            balance.js cash_flow.js profit.js
                excel数据的读取及处理 页面的操作

            company_fhq_prompt.js
                孵化器的操作
                    验证企业信息并通过审核
                    驳回企业提交的信息

            companyinfo_change_view.js
                修改企业对象页面 核心成员中教育经历和工作经历显示的问题

            companyinforeportadmin.js
                生成企业报告时所需的js

            opt_evaluation.js
                修改企业，孵化器及平台评价样式的js

            set_head.js
                设置机构用户 企业报告和信息的页面显示

            xlsx.full.min.js
                excel操作用到的js库

        lightbox
            孵化器查看企业营业执照的放大图

        upload
            企业营业执照存放位置

    templates
        balance.html cash_flow_html profit.html
            财务报表页面
        company_status.html
            企业进度流程页面


incubator 孵化器相关

index 登陆 平台用户 相关
    static
        js
            base.js 全局的js
                1 删除change_view模板中的 ‘另一个’ 添加另一个改为添加
                2 设置侧边栏和面包屑的数据
                3 设置 /admin/auth/user/res_in 页面的面包屑

            change_name_to_phone.js
                把名字改为电话 超管的电话实际是lastname字段实现的

            deal_bug.js
                平台用户 加减分项 用到了外键自动补全
                django_extensions 外键自动补全功能出现问题 用js进行了修补

            debug_rejectreasonadmin.js
                在孵化器驳回理由对象页面 删除对企业信息的修改按钮

            debug_reportbackadmin.js
                机构返回页面 删除对机构信息的修改按钮
                
            status.js
                企业提交数据前进行确认
    templates
        staff.html
            企业等待孵化器审批页面
        其他
            登陆注册页面 孵化器机构注册页面

    my_context_processors.py
        全局模板传参模块


middleware
    中间件
    通过用户类型的不同 获得不同的侧边栏








http://35.201.129.75:8002
管理员 
    账号 miss 密码 mi123456
其他用户密码均为 123123


创建超级用户
设置组
    企业用户
        company
    孵化器用户
        company—change incubator
    机构用户
        company—change institution






目录结构说明
    整个工作在index中完成
    需要先注册 /register


问题
    表格e37 有 e36 而d37无 d36