from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# 获奖名称 行业领域1 有问题的

'''
CompanyInfo
    Shareholder
    Enterprise_Awards
    personal_Awards
    Project
    Patent
    Drug_approval
    MIRC
    Standard_setting
    Core_member
        Education_experience
        work_experience


'''




x1_d = ((1 ,'集成电路布图'),  (2 ,'其他'))
class CompanyInfo(models.Model):
    '一、基本信息'
    user = models.OneToOneField(User)
    name = models.CharField(max_length=50,verbose_name='企业名称',blank=True,null=True)
    create_date = models.DateField(verbose_name='成立时间',blank=True,null=True)
    registered_capital = models.IntegerField(verbose_name='注册资本（万元）',blank=True,null=True)
    paid_in_capital = models.IntegerField(verbose_name='实收资本（万元）',blank=True,null=True)
    major_business = models.CharField(max_length=50,verbose_name='主营产品（或服务）',blank=True,null=True)
    work_force = models.IntegerField(verbose_name='职工总数',blank=True,null=True)
    junior_college_number = models.IntegerField(verbose_name='大专以上学历人数',blank=True,null=True)
    developer_number = models.IntegerField(verbose_name='从事研发人员数',blank=True,null=True)


    is_high_tech_enterprise = models.BooleanField(verbose_name='是否是高新技术企业',default=False)
    abouts = models.CharField(max_length=500,verbose_name='企业简介',blank=True,null=True)

    # {1 :'电子信息',  2 :'互联网及移动互联网', 3 :'生物医药', 4 :'先进制造', 5 :'新能源及节能环保', 6 :'新材料', 7 :'其他',}
    field_1 = models.SmallIntegerField(verbose_name='行业领域1',blank=True,null=True)
    field_2 = models.CharField(max_length=20,verbose_name='行业领域2',blank=True,null=True)

    # ???
    # 
    x1 = models.SmallIntegerField(choices=x1_d,verbose_name='',blank=True,null=True)

    # {1:'独立知识产权', 2:'合作研发', 3:'购买技术', 4:'其他'}
    technical_source = models.SmallIntegerField(verbose_name='技术来源',blank=True,null=True)
    
    # Source of achievement transformation
    # {1:'高校/科研院所', 2:'相关科技计划', 3:'自行研发', 4:'其他'}
    SOAT = models.SmallIntegerField(verbose_name='成果转化来源',blank=True,null=True)


    def __str__(self):
        if self.name:
            return self.name
        else:
            return '无名企业'

    class Meta:
        verbose_name='一、基本信息'
        verbose_name_plural=verbose_name


class Shareholder(models.Model):
    '主要股东及股权比例（前五名）'
    companyInfo = models.ForeignKey(CompanyInfo,verbose_name='企业',blank=True,null=True)
    name = models.CharField(max_length=50,verbose_name='股东名称',blank=True,null=True)
    share_ratio = models.FloatField(verbose_name='股权比例',blank=True,null=True)

    # {1:'货币出资', 2:'实物', 3:'知识产权', 4:'土地使用权' ,5:'其他'}
    form_of_contribution = models.SmallIntegerField(verbose_name='出资形式',blank=True,null=True)

    class Meta:
        verbose_name='主要股东及股权比例（前五名）'
        verbose_name_plural=verbose_name

class EnterpriseAwards(models.Model):
    '企业获奖情况'
    companyInfo = models.ForeignKey(CompanyInfo,verbose_name='企业',blank=True,null=True)
    level = models.CharField(max_length=10,verbose_name='获奖级别',blank=True,null=True)
    title = models.CharField(max_length=50,verbose_name='获奖名称',blank=True,null=True)
    date = models.DateField(verbose_name='获奖时间',blank=True,null=True)
    
    class Meta:
        verbose_name='企业获奖情况'
        verbose_name_plural=verbose_name

class PersonalAwards(models.Model):
    '核心团队个人获奖情况'
    companyInfo = models.ForeignKey(CompanyInfo,verbose_name='企业',blank=True,null=True)
    name = models.CharField(max_length=10,verbose_name='获奖人',blank=True,null=True)
    level_title = models.CharField(max_length=50,verbose_name='获奖级别/名称',blank=True,null=True)
    date = models.DateField(verbose_name='获奖时间',blank=True,null=True)
    
    class Meta:
        verbose_name='核心团队个人获奖情况'
        verbose_name_plural=verbose_name

class Project(models.Model):
    '企业曾经承担或正在承担的科技计划项目'
    companyInfo = models.ForeignKey(CompanyInfo,verbose_name='企业',blank=True,null=True)
    _type = models.CharField(max_length=10,verbose_name='计划类别',blank=True,null=True)
    title = models.CharField(max_length=50,verbose_name='立项名称',blank=True,null=True)
    create_date = models.DateField(verbose_name='立项时间',blank=True,null=True)
    finished_date_and_conclusion = models.CharField(max_length=50,verbose_name='结项时间/结论',blank=True,null=True)
    
    class Meta:
        verbose_name='企业曾经承担或正在承担的科技计划项目'
        verbose_name_plural=verbose_name

# 企业核心技术知识产权情况（可复选）
class Patent(models.Model):
    '专利'
    companyInfo = models.ForeignKey(CompanyInfo,verbose_name='企业',blank=True,null=True)
    title = models.CharField(max_length=50,verbose_name='专利名',blank=True,null=True)
    _type = models.CharField(max_length=50,verbose_name='专利类型',blank=True,null=True)
    num = models.CharField(max_length=50,verbose_name='专利号',blank=True,null=True)
    date = models.DateField(verbose_name='获得时间',blank=True,null=True)

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
    
    class Meta:
        verbose_name='标准制定情况'
        verbose_name_plural=verbose_name

class CoreMember(models.Model):
    '  核心团队（至少填三人）'
    companyInfo = models.ForeignKey(CompanyInfo,verbose_name='企业',blank=True,null=True)
    name = models.CharField(max_length=50,verbose_name='姓名',blank=True,null=True)
    # 1 男 2 女
    gender = models.SmallIntegerField(verbose_name='性别',blank=True,null=True)
    age = models.SmallIntegerField(verbose_name='年龄',blank=True,null=True)
    position = models.CharField(max_length=50,verbose_name='职位',blank=True,null=True)
    is_study_abroad = models.BooleanField(verbose_name='留学经历',default=False)
    entrepreneurial_times = models.SmallIntegerField(verbose_name='创业次数',blank=True,null=True)

    experience = models.CharField(max_length=500,verbose_name='谈对自己创业最重要的一个经历',blank=True,null=True)
    
    def __str__(self):
        return self.name

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
    date_s = models.DateField(verbose_name='工作时间_开始',blank=True,null=True)
    date_e = models.DateField(verbose_name='工作时间_结束',blank=True,null=True)
    
    class Meta:
        verbose_name='工作经历（可增加）'
        verbose_name_plural=verbose_name




class FinancialSituation(models.Model):
    '二、财务状况'
    companyInfo = models.ForeignKey(CompanyInfo,verbose_name='企业',blank=True,null=True)
    income = models.IntegerField(verbose_name='累计销售收入',blank=True,null=True)
    profit = models.IntegerField(verbose_name='累计净利润',blank=True,null=True)
    total = models.IntegerField(verbose_name='期末总资产',blank=True,null=True)
    r_d_cost = models.IntegerField(verbose_name='研发费用总额',blank=True,null=True)

    class Meta:
        verbose_name='二、财务状况'
        verbose_name_plural=verbose_name

class ProductsAndMarket(models.Model):
    '三、产品与市场'
    companyInfo = models.OneToOneField(CompanyInfo,verbose_name='企业',blank=True,null=True)
    product = models.CharField(max_length=500,verbose_name='主营产品（或服务）',blank=True,null=True)
    model = models.CharField(max_length=500,verbose_name='商业模式',blank=True,null=True)
    analysis_forecast = models.CharField(max_length=500,verbose_name='市场分析及前景预测',blank=True,null=True)

    class Meta:
        verbose_name='三、产品与市场'
        verbose_name_plural=verbose_name

class TechnologyRD(models.Model):
    '四、技术与研发'
    companyInfo = models.OneToOneField(CompanyInfo,verbose_name='企业',blank=True,null=True)
    status = models.CharField(max_length=500,verbose_name='核心技术及研发情况',blank=True,null=True)

    class Meta:
        verbose_name='四、技术与研发'
        verbose_name_plural=verbose_name

class ServerRequest(models.Model):
    '五、服务需求'
    companyInfo = models.OneToOneField(CompanyInfo,verbose_name='企业')
    amount = models.IntegerField(verbose_name='融资金额（万元）',blank=True,null=True)
    duration = models.SmallIntegerField(verbose_name='融资时间',blank=True,null=True)
    # 股权融资
    ratio = models.FloatField(verbose_name='拟出让股权比例',blank=True,null=True)
    # 债权融资
    interest_rate = models.FloatField(verbose_name='可以接受的最高年利率%',blank=True,null=True)
    plan = models.CharField(max_length=500,verbose_name='资金使用计划',blank=True,null=True)
    small_loan = models.SmallIntegerField(verbose_name='小额贷款',blank=True,null=True)
    # ((1,'主板'),(2,'中小板'),(3,'创业板'),(4,'新三板'),(5,'上海股权托管交易中心'),(6,'培训辅导'),(7,'上市路演需求'))
    share_model = models.SmallIntegerField(verbose_name='股改、挂牌、上市',blank=True,null=True)
    request = models.CharField(max_length=20,verbose_name='金融服务需求',blank=True,null=True)

    class Meta:
        verbose_name='五、服务需求'
        verbose_name_plural=verbose_name



class IndependentEvaluationOfEnterprises(models.Model):
    external_environment = models.SmallIntegerField(verbose_name='企业所处外部环境（权重：2）',blank=True,null=True)
    products_and_market = models.SmallIntegerField(verbose_name='企业主营产品及市场开拓（权重：2）',blank=True,null=True)
    technology_R_D = models.SmallIntegerField(verbose_name='企业核心技术及研发实力（权重：2）',blank=True,null=True)
    team = models.SmallIntegerField(verbose_name='企业经营及管理团队（权重：4）',blank=True,null=True)

class EvaluationOfEnterprises(models.Model):
    external_environment = models.SmallIntegerField(verbose_name='外部环境（20）',blank=True,null=True)
    products_and_market = models.SmallIntegerField(verbose_name='企业主营产品及市场开拓（20）',blank=True,null=True)
    technology_R_D = models.SmallIntegerField(verbose_name='企业核心技术及研发实力（20）',blank=True,null=True)
    team = models.SmallIntegerField(verbose_name='企业经营及管理团队（40）',blank=True,null=True)

class Balance(models.Model):
    companyInfo = models.OneToOneField(CompanyInfo,verbose_name='企业')
    year = models.SmallIntegerField(verbose_name='年份')
    name = models.CharField(max_length=2)
    value = models.FloatField()






# class Standard_setting(models.Model):
#     '标准制定情况'
#     companyInfo = models.ForeignKey(CompanyInfo,verbose_name='企业')