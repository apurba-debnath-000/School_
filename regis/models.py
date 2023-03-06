from django.db import models

# Create your models here.
class Student(models.Model):
    std_id = models.CharField(max_length=20, default='', blank=True)
    name = models.CharField(max_length=50, default='')
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=40, default='')

