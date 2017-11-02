from django.db import models
from django.contrib.auth.models import User

class Lottery(models.Model):
    name = models.CharField(max_length = 250, blank=True)
    number_balls = models.IntegerField(blank=True, null= True)
    total_number_balls = models.IntegerField(blank=True, null= True)
    date = models.DateField(auto_now=False, auto_now_add= False)


