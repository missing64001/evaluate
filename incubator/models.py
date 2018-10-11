from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Incubator(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=50,verbose_name='孵化器名称',blank=True,null=True)
    phone = models.BigIntegerField(verbose_name='孵化器手机',blank=True,null=True)

    def __str__(self):
        if self.name:
            return self.name
        else:
            return '无名孵化器'

    class Meta:
        verbose_name='孵化器'
        verbose_name_plural=verbose_name