from django.db import models
from django.contrib.auth.models import User
from lottery.models import Lottery

class GeneratedSet(models.Model):
    lottery = models.ForeignKey('Lottery', blank=True, null=True)
    user = models.ForeignKey('User', blank=True, null=True)
    date_time = models.DateTimeField(auto_now=True, auto_now_add= True)

     



