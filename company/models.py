from django.db import models
from django.contrib.auth.models import User
from incubator.models import Incubator
from datetime import timedelta
# Create your models here.

x1_d = ((1 ,'集成电路布图'),  (2 ,'其他'))
status_choices = ((-2,'无效'),
                (-1,'完成'),
                (0,'孵化器审核通过'),
                (1,'填写企业信息完成'),
                (2,'上传财务报表完成'),
                (3,'企业自我评价完成'),
                (4,'企业完成录入提交'),

                (5,'孵化器驳回信息'), #修改后确认提交
                (6,'孵化器审核完成'),
                (7,'孵化器修正评价完成'),

                (8,'平台发送报告'),

                (9,'机构反馈报告'),

                (10,'用户获得反馈'),
            )

field_1_choices = ((1,'A 农、林、牧、渔业'),
                (2,'B 采矿业'),
                (3,'C 制造业'),
                (4,'D 电力、热力、燃气及水生产和供应业'),
                (5,'E 建筑业'),
                (6,'F 批发和零售业'),
                (7,'G 交通运输、仓储和邮政业'),
                (8,'H 住宿和餐饮业'),
                (9,'I 信息传输、软件和信息技术服务业'),
                (10,'J 金融业'),
                (11,'K 房地产业'),
                (12,'L 租赁和商务服务业'),
                (12,'M 科学研究和技术服务业'),
                (13,'N 水利、环境和公共设施管理业'),
                (14,'O 居民服务、修理和其他服务业'),
                (15,'P 教育'),
                (16,'Q 卫生和社会工作'),
                (17,'R 文化、体育和娱乐业'),
                (18,'S 公共管理、社会保障和社会组织'),
                (19,'T 国际组织'),)





technical_source_choices = ((1,'独立知识产权'), (2,'合作研发'), (3,'购买技术'), (4,'其他'))
SOAT_choices = ((1,'高校/科研院所'), (2,'相关科技计划'), (3,'自行研发'), (4,'其他'))
class CompanyInfo(models.Model):
    '一、基本信息'

    user = models.ForeignKey(User,blank=True,null=True)
    status = models.SmallIntegerField(choices=status_choices,verbose_name='状态',default=0)
    incubator = models.ForeignKey(Incubator,verbose_name='所属孵化器',blank=True,null=True)

    name = models.CharField(max_length=50,unique=True,verbose_name='企业名称',blank=True,null=True)
    create_date = models.DateField(verbose_name='成立时间',blank=True,null=True)
    registered_capital = models.IntegerField(verbose_name='注册资本（万元）',blank=True,null=True)
    paid_in_capital = models.IntegerField(verbose_name='实收资本（万元）',blank=True,null=True)
    major_business = models.CharField(max_length=50,verbose_name='主营产品（或服务）',blank=True,null=True)
    work_force = models.IntegerField(verbose_name='职工总数',blank=True,null=True)
    junior_college_number = models.IntegerField(verbose_name='大专以上学历人数',blank=True,null=True)
    developer_number = models.IntegerField(verbose_name='从事研发人员数',blank=True,null=True)


    is_high_tech_enterprise = models.BooleanField(verbose_name='是否是高新技术企业',default=False)
    abouts = models.TextField(verbose_name='企业简介',blank=True,null=True)

    # 
    field_1 = models.SmallIntegerField(choices=field_1_choices,verbose_name='行业领域',blank=True,null=True)
    field_2 = models.CharField(max_length=20,verbose_name='二级领域',blank=True,null=True)

    # ???
    # 


    credit_code = models.CharField(max_length=50,verbose_name='统一社会信用代码',blank=True,null=True)
    phone = models.CharField(verbose_name='联系电话',max_length=20,blank=True,null=True)
    business_license_pic = models.ImageField(upload_to='upload',blank=True,null=True)


    def __str__(self):
        if self.name:
            return self.name
        else:
            return '无名企业'

    class Meta:
        verbose_name='一、基本信息'
        verbose_name_plural=verbose_name

class RejectReason(models.Model):
    companyInfo = models.ForeignKey(CompanyInfo,verbose_name='企业',blank=True,null=True)
    text = models.TextField(verbose_name='拒绝原因',blank=True,null=True)
    is_alive = models.BooleanField(verbose_name='是否有效',default=True)    
    create_date = models.DateTimeField(verbose_name='生成时间',auto_now_add=True,blank=True,null=True)

    def __str__(self):
        if len(self.text) < 10:
            return self.text
        else:
            return self.text[:8] + '...'

    class Meta:
        verbose_name='驳回理由'
        verbose_name_plural=verbose_name

form_of_contribution_choices = ((1,'货币出资'), (2,'实物'), (3,'知识产权'), (4,'土地使用权') ,(5,'其他'))
class Shareholder(models.Model):
    '主要股东及股权比例（前五名）'
    companyInfo = models.ForeignKey(CompanyInfo,verbose_name='企业',blank=True,null=True)
    name = models.CharField(max_length=50,verbose_name='股东名称',blank=True,null=True)
    share_ratio = models.FloatField(verbose_name='股权比例(%)',blank=True,null=True)

    # {1:'货币出资', 2:'实物', 3:'知识产权', 4:'土地使用权' ,5:'其他'}
    form_of_contribution = models.SmallIntegerField(choices=form_of_contribution_choices,verbose_name='出资形式',blank=True,null=True)

    def __str__(self):
        if self.name:
            return self.name
        else:
            return '-'

    class Meta:
        verbose_name='主要股东及股权比例（前五名）'
        verbose_name_plural=verbose_name

class EnterpriseAwards(models.Model):
    '企业获奖情况'
    companyInfo = models.ForeignKey(CompanyInfo,verbose_name='企业',blank=True,null=True)
    level = models.CharField(max_length=10,verbose_name='获奖级别',blank=True,null=True)
    title = models.CharField(max_length=50,verbose_name='获奖名称',blank=True,null=True)
    date = models.DateField(verbose_name='获奖时间',blank=True,null=True)
    
    def __str__(self):
        if self.title:
            return self.title
        else:
            return '-'

    class Meta:
        verbose_name='企业获奖情况'
        verbose_name_plural=verbose_name

class PersonalAwards(models.Model):
    '核心团队个人获奖情况'
    companyInfo = models.ForeignKey(CompanyInfo,verbose_name='企业',blank=True,null=True)
    name = models.CharField(max_length=10,verbose_name='获奖人',blank=True,null=True)
    level_title = models.CharField(max_length=50,verbose_name='获奖级别/名称',blank=True,null=True)
    date = models.DateField(verbose_name='获奖时间',blank=True,null=True)
    
    def __str__(self):
        if self.name:
            return self.name
        else:
            return '-'

    class Meta:
        verbose_name='核心团队个人获奖情况'
        verbose_name_plural=verbose_name

class Project(models.Model):
    '企业曾经承担或正在承担的科技计划项目'
    companyInfo = models.ForeignKey(CompanyInfo,verbose_name='企业',blank=True,null=True)
    _type = models.CharField(max_length=10,verbose_name='计划类别',blank=True,null=True)
    title = models.CharField(max_length=50,verbose_name='立项名称',blank=True,null=True)
    create_date = models.DateField(verbose_name='立项时间',blank=True,null=True)
    finished_date = models.DateField(verbose_name='结项时间',blank=True,null=True)
    conclusion = models.TextField(verbose_name='结论',blank=True,null=True)
    
    def __str__(self):
        if self.title:
            return self.title
        else:
            return '-'

    class Meta:
        verbose_name='企业曾经承担或正在承担的科技计划项目'
        verbose_name_plural=verbose_name

# 企业核心技术知识产权情况（可复选）
class Patent(models.Model):
    '专利'
    _type_choices = ((1,'发明专利') ,(2,'实用新型专利') ,(3,'外观设计') ,(4,'软件著作权'))
    companyInfo = models.ForeignKey(CompanyInfo,verbose_name='企业',blank=True,null=True)
    title = models.CharField(max_length=50,verbose_name='专利名',blank=True,null=True)
    _type = models.SmallIntegerField(choices=_type_choices,verbose_name='专利类型',blank=True,null=True)
    num = models.CharField(max_length=50,verbose_name='专利号',blank=True,null=True)
    date = models.DateField(verbose_name='获得时间',blank=True,null=True)

    def __str__(self):
        if self.title:
            return self.title
        else:
            return '-'

    class Meta:
        verbose_name='专利'
        verbose_name_plural=verbose_name

class DrugApproval(models.Model):
    '药品批文'
    companyInfo = models.ForeignKey(CompanyInfo,verbose_name='企业',blank=True,null=True)
    title = models.CharField(max_length=50,verbose_name='药品名称',blank=True,null=True)
    new_drug = models.CharField(max_length=50,verbose_name='国家新药',blank=True,null=True)
    c_drug = models.CharField(max_length=50,verbose_name='国家一级中药保护品种',blank=True,null=True)
    num = models.CharField(max_length=50,verbose_name='  药品批准文号 ',blank=True,null=True)
    effective_date = models.DateField(verbose_name='有效日期',blank=True,null=True)
    
    def __str__(self):
        if self.title:
            return self.title
        else:
            return '-'

    class Meta:
        verbose_name='药品批文'
        verbose_name_plural=verbose_name

class MIRC(models.Model):
    '医疗器械注册证' 
    'Medical instrument registration certificate'
    companyInfo = models.ForeignKey(CompanyInfo,verbose_name='企业',blank=True,null=True)
    title = models.CharField(max_length=50,verbose_name='产品名称',blank=True,null=True)
    num = models.CharField(max_length=50,verbose_name='  医疗器械注册号 ',blank=True,null=True)
    effective_date = models.DateField(verbose_name='有效日期',blank=True,null=True)
    
    def __str__(self):
        if self.title:
            return self.title
        else:
            return '-'

    class Meta:
        verbose_name='医疗器械注册证'
        verbose_name_plural=verbose_name

class StandardSetting(models.Model):
    '标准制定情况'
    companyInfo = models.ForeignKey(CompanyInfo,verbose_name='企业',blank=True,null=True)
    title = models.CharField(max_length=50,verbose_name='标准名称',blank=True,null=True)
    level = models.CharField(max_length=10,verbose_name='标准级别',blank=True,null=True)
    num = models.CharField(max_length=50,verbose_name='  标准编号 ',blank=True,null=True)

    # 1 牵头 2 参与
    status = models.SmallIntegerField(verbose_name='起草单位中的地位',blank=True,null=True)
    
    def __str__(self):
        if self.title:
            return self.title
        else:
            return '-'

    class Meta:
        verbose_name='标准制定情况'
        verbose_name_plural=verbose_name

class Otherm(models.Model):
    companyInfo = models.OneToOneField(CompanyInfo,verbose_name='企业',blank=True,null=True)
    x1 = models.SmallIntegerField(choices=x1_d,verbose_name='',blank=True,null=True)

    # {1:'独立知识产权', 2:'合作研发', 3:'购买技术', 4:'其他'}
    technical_source = models.SmallIntegerField(choices=technical_source_choices,verbose_name='技术来源',blank=True,null=True)
    
    # Source of achievement transformation
    # {1:'高校/科研院所', 2:'相关科技计划', 3:'自行研发', 4:'其他'}
    SOAT = models.SmallIntegerField(choices=SOAT_choices,verbose_name='成果转化来源',blank=True,null=True)
    def __str__(self):
        return '其他'

    class Meta:
        verbose_name='其他'
        verbose_name_plural=verbose_name

class CoreMember(models.Model):
    '  核心团队（至少填三人）'
    companyInfo = models.ForeignKey(CompanyInfo,verbose_name='企业',blank=True,null=True)
    name = models.CharField(max_length=50,verbose_name='姓名',blank=True,null=True)
    # 1 男 2 女
    gender = models.SmallIntegerField(choices=((1,'男'),(2,'女')),verbose_name='性别',blank=True,null=True)
    age = models.SmallIntegerField(verbose_name='年龄',blank=True,null=True)
    position = models.CharField(max_length=50,verbose_name='职位',blank=True,null=True)
    is_study_abroad = models.BooleanField(verbose_name='留学经历',default=False)
    entrepreneurial_times = models.SmallIntegerField(verbose_name='创业次数',blank=True,null=True)
    experience = models.TextField(max_length=500,verbose_name='谈对自己创业最重要的一个经历',blank=True,null=True)


    xxtemp1 = models.BooleanField(verbose_name='教育经历1',default=False)
    education1 = models.CharField(max_length=50,verbose_name='学历',blank=True,null=True)
    university1 = models.CharField(max_length=50,verbose_name='毕业院校',blank=True,null=True)
    major1 = models.CharField(max_length=50,verbose_name='专业',blank=True,null=True)

    xxtemp2 = models.BooleanField(verbose_name='教育经历2',default=False)
    education2 = models.CharField(max_length=50,verbose_name='学历',blank=True,null=True)
    university2 = models.CharField(max_length=50,verbose_name='毕业院校',blank=True,null=True)
    major2 = models.CharField(max_length=50,verbose_name='专业',blank=True,null=True)

    xxtemp3 = models.BooleanField(verbose_name='教育经历3',default=False)
    education3 = models.CharField(max_length=50,verbose_name='学历',blank=True,null=True)
    university3 = models.CharField(max_length=50,verbose_name='毕业院校',blank=True,null=True)
    major3 = models.CharField(max_length=50,verbose_name='专业',blank=True,null=True)


    xxtempgz1 = models.BooleanField(verbose_name='工作经历1',default=False)
    company1 = models.CharField(max_length=50,verbose_name='工作单位',blank=True,null=True)
    position1 = models.CharField(max_length=50,verbose_name='职位',blank=True,null=True)
    date_s1 = models.DateField(verbose_name='开始',blank=True,null=True)
    date_e1 = models.DateField(verbose_name='结束',blank=True,null=True)

    xxtempgz2 = models.BooleanField(verbose_name='工作经历2',default=False)
    company2 = models.CharField(max_length=50,verbose_name='工作单位',blank=True,null=True)
    position2 = models.CharField(max_length=50,verbose_name='职位',blank=True,null=True)
    date_s2 = models.DateField(verbose_name='开始',blank=True,null=True)
    date_e2 = models.DateField(verbose_name='结束',blank=True,null=True)

    xxtempgz3 = models.BooleanField(verbose_name='工作经历3',default=False)
    company3 = models.CharField(max_length=50,verbose_name='工作单位',blank=True,null=True)
    position3 = models.CharField(max_length=50,verbose_name='职位',blank=True,null=True)
    date_s3 = models.DateField(verbose_name='开始',blank=True,null=True)
    date_e3 = models.DateField(verbose_name='结束',blank=True,null=True)

    def __str__(self):
        if self.name:
            return self.name
        return ''

    class Meta:
        verbose_name='  核心团队(至少三人)'
        verbose_name_plural=verbose_name

class EducationExperience(models.Model):
    '教育经历（可增加）'
    core_member = models.ForeignKey(CoreMember,verbose_name='核心团队',blank=True,null=True)
    education = models.CharField(max_length=50,verbose_name='学历',blank=True,null=True)
    university = models.CharField(max_length=50,verbose_name='毕业院校',blank=True,null=True)
    major = models.CharField(max_length=50,verbose_name='专业',blank=True,null=True)
    
    class Meta:
        verbose_name='教育经历（可增加）'
        verbose_name_plural=verbose_name

class WorkExperience(models.Model):
    '工作经历（可增加）'
    core_member = models.ForeignKey(CoreMember,verbose_name='核心团队',blank=True,null=True)
    company = models.CharField(max_length=50,verbose_name='工作单位',blank=True,null=True)
    position = models.CharField(max_length=50,verbose_name='职位',blank=True,null=True)
    date_s = models.DateField(verbose_name='开始',blank=True,null=True)
    date_e = models.DateField(verbose_name='结束',blank=True,null=True)
    
    class Meta:
        verbose_name='工作经历（可增加）'
        verbose_name_plural=verbose_name



class FinancialSituation(models.Model):
    '二、财务状况'
    companyInfo = models.ForeignKey(CompanyInfo,verbose_name='企业',blank=True,null=True)
    year = models.SmallIntegerField(verbose_name='年份',blank=True,null=True)
    income = models.IntegerField(verbose_name='累计销售收入（万元）',blank=True,null=True)
    profit = models.IntegerField(verbose_name='累计净利润（万元）',blank=True,null=True)
    total = models.IntegerField(verbose_name='期末总资产（万元）',blank=True,null=True)
    r_d_cost = models.IntegerField(verbose_name='研发费用总额（万元）',blank=True,null=True)

    def __str__(self):
        if self.year:
            return str(self.year)
        else:
            return '-'
   
        
    class Meta:
        verbose_name='二、财务状况'
        verbose_name_plural=verbose_name

class ProductsAndMarket(models.Model):
    '三、产品与市场'
    companyInfo = models.OneToOneField(CompanyInfo,verbose_name='企业',blank=True,null=True)
    product = models.TextField(verbose_name='主营产品（或服务）',blank=True,null=True)
    model = models.TextField(verbose_name='商业模式',blank=True,null=True)
    analysis_forecast = models.TextField(verbose_name='市场分析及前景预测',blank=True,null=True)
   
    def __str__(self):
        return '产品与市场'
        
    class Meta:
        verbose_name='三、产品与市场'
        verbose_name_plural=verbose_name

class TechnologyRD(models.Model):
    '四、技术与研发'
    companyInfo = models.OneToOneField(CompanyInfo,verbose_name='企业',blank=True,null=True)
    status = models.TextField(verbose_name='核心技术及研发情况',blank=True,null=True)
   
    def __str__(self):
        return '技术与研发'

    class Meta:
        verbose_name='四、技术与研发'
        verbose_name_plural=verbose_name


share_model_choices = ((1,'主板'),(2,'中小板'),(3,'创业板'),(4,'新三板'),(5,'上海股权托管交易中心'),(6,'培训辅导'),(7,'上市路演需求'))
class ServerRequest(models.Model):
    '五、服务需求'
    companyInfo = models.OneToOneField(CompanyInfo,verbose_name='企业')
    amount = models.IntegerField(verbose_name='融资金额（万元）',blank=True,null=True)
    duration = models.SmallIntegerField(verbose_name='融资时间（天）',blank=True,null=True)
    # 股权融资
    ratio = models.FloatField(verbose_name='拟出让股权比例（%）',blank=True,null=True)
    # 债权融资
    interest_rate = models.FloatField(verbose_name='可以接受的最高年利率（%）',blank=True,null=True)
    plan = models.TextField(verbose_name='资金使用计划',blank=True,null=True)
    small_loan = models.SmallIntegerField(verbose_name='小额贷款（万元）',blank=True,null=True)
    # 
    share_model = models.SmallIntegerField(choices=share_model_choices,verbose_name='股改、挂牌、上市',blank=True,null=True)
    request = models.TextField(verbose_name='科技金融服务需求',blank=True,null=True)
    otherrequest = models.TextField(verbose_name='其他科技服务需求',blank=True,null=True)
    # img = models.ImageField(upload_to='static/img/',blank=True,null=True)
    
    def __str__(self):
        return '服务需求'

    class Meta:
        verbose_name='五、服务需求'
        verbose_name_plural=verbose_name


external_environment_choices=((1,'1分'),
                              (2,'2分'),
                              (3,'3分'),
                              (4,'4分'),
                              (5,'5分'),
                              (6,'6分'),
                              (7,'7分'),
                              (8,'8分'),
                              (9,'9分'),
                              (10,'10分'),
                                )
class IndependentEvaluationOfEnterprises(models.Model):
    companyInfo = models.OneToOneField(CompanyInfo,verbose_name='企业',blank=True,null=True)
    external_environment = models.SmallIntegerField(choices=external_environment_choices,verbose_name='企业所处外部环境（权重：2）',default=1,blank=True,null=True)
    products_and_market = models.SmallIntegerField(choices=external_environment_choices,verbose_name='企业主营产品及市场开拓（权重：2）',default=1,blank=True,null=True)
    technology_R_D = models.SmallIntegerField(choices=external_environment_choices,verbose_name='企业核心技术及研发实力（权重：2）',default=1,blank=True,null=True)
    team = models.SmallIntegerField(choices=external_environment_choices,verbose_name='企业经营及管理团队（权重：4）',default=1,blank=True,null=True)
    create_date = models.DateTimeField(verbose_name='生成时间',auto_now_add=True,blank=True,null=True)

    # def tname(self):
    #     print(type(self.create_date))
    #     verbose_name='自我评价'
    #     verbose_name_plural=verbose_name
    #     return self.companyInfo.name + ' %s' % (self.create_date+ timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return '自主评价'

    class Meta:
        verbose_name='自主评价'
        verbose_name_plural=verbose_name


class EvaluationOfEnterprises(models.Model):
    companyInfo = models.OneToOneField(CompanyInfo,verbose_name='企业',blank=True,null=True)
    external_environment = models.SmallIntegerField(choices=external_environment_choices,verbose_name='企业所处外部环境（权重：2）',blank=True,null=True)
    products_and_market = models.SmallIntegerField(choices=external_environment_choices,verbose_name='企业主营产品及市场开拓（权重：2）',blank=True,null=True)
    technology_R_D = models.SmallIntegerField(choices=external_environment_choices,verbose_name='企业核心技术及研发实力（权重：2）',blank=True,null=True)
    team = models.SmallIntegerField(choices=external_environment_choices,verbose_name='企业经营及管理团队（权重：4）',blank=True,null=True)
    create_date = models.DateTimeField(verbose_name='生成时间',auto_now_add=True,blank=True,null=True)
    
    def __str__(self):
        return '校正评价'

    class Meta:
        verbose_name='校正评价'
        verbose_name_plural=verbose_name

class Balance(models.Model):
    companyInfo = models.ForeignKey(CompanyInfo,verbose_name='企业',blank=True,null=True)
    year = models.SmallIntegerField(verbose_name='年份',blank=True,null=True)
    name = models.CharField(max_length=4)
    value = models.FloatField()

    def __str__(self):
        if self.year:
            return str(self.year)
        return ''

    class Meta:
        verbose_name='资产负债表'
        verbose_name_plural=verbose_name

class Profit(models.Model):
    companyInfo = models.ForeignKey(CompanyInfo,verbose_name='企业',blank=True,null=True)
    year = models.SmallIntegerField(verbose_name='年份',blank=True,null=True)
    name = models.CharField(max_length=4)
    value = models.FloatField()

    def __str__(self):
        if self.year:
            return str(self.year)
        return ''

    class Meta:
        verbose_name='利润表'
        verbose_name_plural=verbose_name

class CashFlow(models.Model):
    companyInfo = models.ForeignKey(CompanyInfo,verbose_name='企业',blank=True,null=True)
    year = models.SmallIntegerField(verbose_name='年份',blank=True,null=True)
    name = models.CharField(max_length=4)
    value = models.FloatField()

    def __str__(self):
        if self.year:
            return str(self.year)
        return ''

    class Meta:
        verbose_name='现金流量表'
        verbose_name_plural=verbose_name









def get_user_group(request,groupname=None):

    try:
        user = request.user
    except Exception:
        user = request
    if user.is_anonymous:
        return None

    if user.is_superuser:
        if not groupname:
            return 'super'
        else:
            mygname = 'super'
    elif not  groupname:
        if user.groups.all():
            return user.groups.all()[0].name
    else:
        if user.groups.all():
            mygname = user.groups.all()[0].name
        else:
            mygname = None
    return mygname == groupname
