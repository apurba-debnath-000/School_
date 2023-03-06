from django.db import models
from .managers import CustomManager

class StudentEnrollment(models.Model):
    student_name = models.CharField(max_length=70)
    student_roll = models.IntegerField()
    student_marks = models.IntegerField()
    student_grade = models.CharField(max_length=40)

    objects = models.Manager()
    #students = models.Manager()# default model manager overriding.
    #students = CustomManager()
#To get different behaviour:
class ProxyStudent(StudentEnrollment):
    students = CustomManager()
    class Meta:
        proxy = True
        ordering = ['student_name']

    
