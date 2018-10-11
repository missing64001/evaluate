from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Institution(models.Model):
    user = models.OneToOneField(User)
    type = models.SmallIntegerField(choices=((1 ,'投资'),  (2 ,'银行')),verbose_name='机构类型',blank=True,null=True)
    name = models.CharField(max_length=50,verbose_name='机构名称',blank=True,null=True)
    phone = models.BigIntegerField(verbose_name='机构手机',blank=True,null=True)
    
    def __str__(self):
        if self.name:
            return self.name
        else:
            return '无名机构'

    class Meta:
        verbose_name='机构'
        verbose_name_plural=verbose_name