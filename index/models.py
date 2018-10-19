from django.db import models
from django.contrib.auth.models import User
from company.models import CompanyInfo


bonus_items = ((1,'科技部科小认定'),(2,'市科技计划项目'),(3,'创业大赛'),(4,'其他'))
class Bonus(models.Model):
    companyInfo = models.ForeignKey(CompanyInfo,verbose_name='企业')
    item = models.SmallIntegerField(verbose_name='加分项',choices=bonus_items)
    note = models.TextField(verbose_name='加分说明')
    value = models.SmallIntegerField(verbose_name='分值')

    def __str__(self):
        return self.companyInfo.name

    class Meta:
        verbose_name='加分项'
        verbose_name_plural=verbose_name

subtraction_items = ((1,'房屋信息通报'),(2,'经营者社会评价'),(3,'其他'))  
class Subtraction(models.Model):
    companyInfo = models.ForeignKey(CompanyInfo,verbose_name='企业',blank=True,null=True)
    item = models.SmallIntegerField(verbose_name='减分项',choices=subtraction_items,blank=True,null=True)
    note = models.TextField(verbose_name='减分说明',blank=True,null=True)
    value = models.SmallIntegerField(verbose_name='分值',blank=True,null=True)

    def __str__(self):
        return self.companyInfo.name

    class Meta:
        verbose_name='减分项'
        verbose_name_plural=verbose_name






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




# class Standard_setting(models.Model):
#     '标准制定情况'
#     companyInfo = models.ForeignKey(CompanyInfo,verbose_name='企业')