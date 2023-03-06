from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class StudentNew(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key= True)
    name = models.CharField(max_length=70)
    roll = models.IntegerField(unique = True, null = False)
    city = models.CharField(max_length=40)
    marks = models.IntegerField()
    grade = models.CharField(max_length=40)
    pass_date = models.DateField()
    adm_dateTime_field = models.DateTimeField()

    
