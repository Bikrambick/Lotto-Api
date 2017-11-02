from django.db import models
from django.contrib.auth.models import User
from lottery.models import Lottery

class GeneratedSet(models.Model):
    lottery = models.ForeignKey(Lottery, on_delete = models.CASCADE)
    date_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    nb_of_odds = models.IntegerField(null = True)
    flag_for_odds = models.BooleanField(default = False)
    timing = models.IntegerField()
    nb_0f_b20 = models.IntegerField(null=True)
    flag_for_b20 = models.BooleanField(default = False)
    score_range_top = models.IntegerField(null = True)
    score_range_bottom = models.IntegerField(null = True)
    flag_for_score = models.BooleanField(default = False)
    set_score = models.IntegerField()
    prev_rep_nb = models.IntegerField(null=True)
    flag_for_prev_rep = models.BooleanField(default = False)
    nb_to_Inc = models.CharField(max_length = 50)
    nb_of_games = models.IntegerField()
    failed_flag = models.BooleanField(default = False)