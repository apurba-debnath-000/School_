from django.contrib import admin
from . import models
from .models import StudentEnrollment, ProxyStudent
# Register your models here.

@admin.register(StudentEnrollment)
class StudentEnrollAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'student_name',
        'student_roll',
        'student_marks',
        'student_grade',
    
     ]
    
@admin.register(ProxyStudent)
class ProxyStudentAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'student_name',
        'student_roll',
        'student_marks',
        'student_grade',
    
     ]
