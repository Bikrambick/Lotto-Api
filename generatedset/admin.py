from django.contrib import admin
from .models import GeneratedSet

# Register your models here.
@admin.register(GeneratedSet)
class AdminGeneratedSet(admin.ModelAdmin):
    list_display = ('user', )