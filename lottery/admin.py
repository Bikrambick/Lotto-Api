from django.contrib import admin
from .models import Lottery
# Register your models here.
@admin.register(Lottery)
class AdminLottery(admin.ModelAdmin):
    list_display = ('name', )