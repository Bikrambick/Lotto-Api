from django.contrib import admin
from .models import Ticket
# Register your models here.
@admin.register(Ticket)
class AdminTicket(admin.ModelAdmin):
    list_display = ('name', )