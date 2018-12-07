from django.db import models
from django.contrib.auth.models import User
from company.models import CompanyInfo 
import re
from datetime import timedelta

# Create your models here.
# 
# 

class Institution(models.Model):
    user = models.OneToOneField(User)
    type = models.SmallIntegerField(choices=((1 ,'投资'),  (2 ,'银行')),verbose_name='机构类型',blank=True,null=True)
    name = models.CharField(max_length=50,unique=True,verbose_name='机构名称',blank=True,null=True)
    phone = models.CharField(verbose_name='联系电话',max_length=20,blank=True,null=True)
    
    def __str__(self):
        if self.name:
            return self.name
        else:
            return '无名机构'

    class Meta:
        verbose_name='机构'
        verbose_name_plural=verbose_name



# bank_report
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
invest_report_items = (
    '1.外部环境（20）',
    '2、企业主营产品及市场开拓（20）',
    '3、企业核心技术及研发实力（20）',
    '4、企业经营及管理团队（40）',
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


class InvestReport(models.Model):
    institution = models.ManyToManyField(Institution,verbose_name='请选择推荐的机构')

    companyInfo = models.ForeignKey(CompanyInfo,verbose_name='企业')

    for i in enumerate(invest_report_items[:4],1):
        exec("i%s = models.SmallIntegerField(choices=external_environment_choices,verbose_name='%s',default=1,blank=True,null=True)"%i)
    for i in enumerate(invest_report_items[4:],5):
        exec("i%s = models.BooleanField(verbose_name='%s',choices = ((0,'%s分'),(1,'%s分')),default=False)"%(*i,'0',re.findall(r'\d+',i[1])[0]))

    create_date = models.DateTimeField(verbose_name='生成时间',auto_now=True,blank=True,null=True)

    def __str__(self):
        return (self.create_date+ timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")

    class Meta:
        verbose_name='发送投资类金融报告'
        verbose_name_plural=verbose_name





bank_report_items = (
    '1.外部环境（20）',
    '2、企业主营产品及市场开拓（20）',
    '3、企业核心技术及研发实力（20）',
    '4、企业经营及管理团队（40）',
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
    '研发费用收入比例(10)',
    )

class BankReport(models.Model):

    institution = models.ManyToManyField(Institution,verbose_name='请选择推荐的机构')
    companyInfo = models.ForeignKey(CompanyInfo,verbose_name='企业')
    for i in enumerate(bank_report_items[:4],1):
        exec("i%s = models.SmallIntegerField(choices=external_environment_choices,verbose_name='%s',default=1,blank=True,null=True)"%i)
    for i in enumerate(bank_report_items[4:],5):
        exec("i%s = models.BooleanField(verbose_name='%s',choices = ((0,'%s分'),(1,'%s分')),default=False)"%(*i,'0',re.findall(r'\d+',i[1])[0]))

    create_date = models.DateTimeField(verbose_name='生成时间',auto_now=True,blank=True,null=True)

    def __str__(self):
        return (self.create_date+ timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")

    class Meta:
        verbose_name='发送银行类金融报告'
        verbose_name_plural=verbose_name



class ReportBack(models.Model):
    institution = models.ForeignKey(Institution,verbose_name='机构',blank=True,null=True)
    investreport = models.ForeignKey(InvestReport,verbose_name='投资类金融报告',blank=True,null=True)
    bankreport = models.ForeignKey(BankReport,verbose_name='投资类金融报告',blank=True,null=True)
    will = models.SmallIntegerField(choices=((1 ,'有意向'),  (2 ,'无意向')),verbose_name='意向',blank=True,null=True)
    type = models.SmallIntegerField(choices=((1 ,'对企业进一步了解'),  (2 ,'与孵化器进一步协调')),verbose_name='选择反馈类别',blank=True,null=True)
    note = models.TextField(verbose_name='反馈内容',blank=True,null=True)
    iscompanyview = models.SmallIntegerField(choices=((1 ,'不可见'),  (2 ,'可见')),verbose_name='对企业是否可见',default=1)
    isinstitutionview = models.SmallIntegerField(choices=((1 ,'不可见'),  (2 ,'可见')),verbose_name='对孵化器是否可见',default=1)



        
    class Meta:
        verbose_name='反馈信息'
        verbose_name_plural=verbose_name


    def __str__(self):
        report = self.investreport or self.bankreport
        return str(report.companyInfo) + ' '+ str(report) + ' 反馈信息'




