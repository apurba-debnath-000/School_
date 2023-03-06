from django.db import models
from django.urls import reverse

# Create your models here.

class Pupils(models.Model):
    p_name = models.CharField(max_length=80)
    p_email = models.EmailField()
    p_roll = models.IntegerField()
    p_course = models.CharField(max_length=60)
    p_password = models.CharField(max_length=20)


    # def get_absolute_url(self):
    #     return reverse('thankyou')
    def get_absolute_url(self):
        return reverse('singleDataView', kwargs={'pk':self.pk})


