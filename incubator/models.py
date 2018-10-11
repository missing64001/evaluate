from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Incubator(models.Model):
    user = models.OneToOneField(User)