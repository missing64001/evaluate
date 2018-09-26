from django.db import models

# Create your models here.
# 获奖名称 行业领域1 有问题的

class CompanyInfo(models.Model):
    name = models.CharField(max_length=50,verbose_name='企业名称')
    create_date = models.DateField(verbose_name='成立时间')
    registered_capital = models.IntegerField(verbose_name='注册资本（万元）')
    paid_in_capital = models.IntegerField(verbose_name='实收资本（万元）')
    major_business = models.CharField(max_length=50,verbose_name='主营产品（或服务）')
    work_force = models.IntegerField(verbose_name='职工总数')
    junior_college_number = models.IntegerField(verbose_name='大专以上学历人数')
    developer_number = models.IntegerField(verbose_name='从事研发人员数')



    is_high_tech_enterprise = models.BooleanField(verbose_name='是否是高新技术企业')
    abouts = models.CharField(max_length=500,verbose_name='企业简介')

    # {1 :'电子信息',  2 :'互联网及移动互联网', 3 :'生物医药', 4 :'先进制造', 5 :'新能源及节能环保', 6 :'新材料', 7 :'其他',}
    field_1 = models.SmallIntegerField(verbose_name='行业领域1')
    field_2 = models.CharField(max_length=20,verbose_name='行业领域2')

    # ???
    # {1 :'集成电路布图',  2 :'其他'}
    x1 = models.SmallIntegerField(verbose_name='x1')

    # {1:'独立知识产权', 2:'合作研发', 3:'购买技术', 4:'其他'}
    technical_source = models.SmallIntegerField(verbose_name='技术来源')
    

    # Source of achievement transformation
    # {1:'高校/科研院所', 2:'相关科技计划', 3:'自行研发', 4:'其他'}
    SOAT = models.SmallIntegerField(verbose_name='成果转化来源')

class Shareholder(models.Model):
    # 主要股东及股权比例（前五名）
    companyInfo = models.ForeignKey(CompanyInfo,verbose_name='企业')
    name = models.CharField(max_length=50,verbose_name='股东名称')
    share_ratio = models.FloatField(verbose_name='股权比例')

    # {1:'货币出资', 2:'实物', 3:'知识产权', 4:'土地使用权' ,5:'其他'}
    form_of_contribution = models.SmallIntegerField(verbose_name='出资形式')

class Enterprise_Awards(models.Model):
    # 企业获奖情况
    companyInfo = models.ForeignKey(CompanyInfo,verbose_name='企业')
    level = models.CharField(max_length=10,verbose_name='获奖级别')
    title = models.CharField(max_length=50,verbose_name='获奖名称')
    date = models.DateField(verbose_name='获奖时间')

class personal_Awards(models.Model):
    # 核心团队个人获奖情况
    companyInfo = models.ForeignKey(CompanyInfo,verbose_name='企业')
    name = models.CharField(max_length=10,verbose_name='获奖人')
    level_title = models.CharField(max_length=50,verbose_name='获奖级别/名称')
    date = models.DateField(verbose_name='获奖时间')
    
class Project(models.Model):
    # 企业曾经承担或正在承担的科技计划项目
    companyInfo = models.ForeignKey(CompanyInfo,verbose_name='企业')
    _type = models.CharField(max_length=10,verbose_name='计划类别')
    title = models.CharField(max_length=50,verbose_name='立项名称')
    create_date = models.DateField(verbose_name='立项时间')
    finished_date_and_conclusion = models.CharField(max_length=50,verbose_name='结项时间/结论')

# 企业核心技术知识产权情况（可复选）
class Patent(models.Model):
    # 专利
    companyInfo = models.ForeignKey(CompanyInfo,verbose_name='企业')
    title = models.CharField(max_length=50,verbose_name='专利名')
    _type = models.CharField(max_length=50,verbose_name='专利类型')
    num = models.CharField(max_length=50,verbose_name='专利号')
    date = models.DateField(verbose_name='获得时间')

class Drug_approval(models.Model):
    # 药品批文
    companyInfo = models.ForeignKey(CompanyInfo,verbose_name='企业')
    title = models.CharField(max_length=50,verbose_name='药品名称')
    new_drug = models.CharField(max_length=50,verbose_name='国家新药')
    c_drug = models.CharField(max_length=50,verbose_name='国家一级中药保护品种')
    num = models.CharField(max_length=50,verbose_name='  药品批准文号 ')
    effective_date = models.DateField(verbose_name='有效日期')

class MIRC(models.Model):
    # 医疗器械注册证 Medical instrument registration certificate
    companyInfo = models.ForeignKey(CompanyInfo,verbose_name='企业')
    title = models.CharField(max_length=50,verbose_name='产品名称')
    num = models.CharField(max_length=50,verbose_name='  医疗器械注册号 ')
    effective_date = models.DateField(verbose_name='有效日期')

class Standard_setting(models.Model):
    # 标准制定情况
    companyInfo = models.ForeignKey(CompanyInfo,verbose_name='企业')
    title = models.CharField(max_length=50,verbose_name='标准名称')
    level = models.CharField(max_length=10,verbose_name='标准级别')
    num = models.CharField(max_length=50,verbose_name='  标准编号 ')

    # 1 牵头 2 参与
    status = models.SmallIntegerField(verbose_name='起草单位中的地位')







