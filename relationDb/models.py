from django.db import models
from django.contrib.auth.models import User


class Page(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    #user = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True)
    #user = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True, limit_choices_to={'is_staff':True})
    page_titile = models.CharField(max_length=60)
    page_no = models.IntegerField()
    page_cat = models.CharField(max_length=60)
    no_likes = models.IntegerField()
