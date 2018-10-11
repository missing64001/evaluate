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




# class Standard_setting(models.Model):
#     '标准制定情况'
#     companyInfo = models.ForeignKey(CompanyInfo,verbose_name='企业')