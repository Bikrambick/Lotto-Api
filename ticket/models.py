from django.db import models
from django.contrib.auth.models import User

class Ticket(models.Model):
    #user = models.OneToOneField(User)
    name = models.CharField(max_length = 250, blank=True)
    numbers = models.CharField(max_length = 250, blank=True)
    draw = models.CharField(max_length = 250, blank=True)
    #game = ''





