from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Pupils)
class PupilAdmin(admin.ModelAdmin):
    list_display = ['id', 'p_name', 'p_email', 'p_roll','p_course','p_password',]