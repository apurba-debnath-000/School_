from django.contrib import admin
from .models import StudentNew

# Register your models here.
@admin.register(StudentNew)
class Student2Admin(admin.ModelAdmin):
    list_display = ['id', 'name','roll', 'city', 'marks','grade', 'pass_date', 'adm_dateTime_field']