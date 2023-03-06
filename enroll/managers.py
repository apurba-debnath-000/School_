from django.db import models


class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('student_name')
    def get_queryset_orderbyid(self):
        return super().get_queryset().order_by('id')
    def get_student_roll_byRange(self, r1, r2):
        return super().get_queryset().filter(student_roll__range=(r1, r2))