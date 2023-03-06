from django.contrib import admin
from .models import Page
# Register your models here.
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['page_titile', 'page_no', 'page_cat', 'no_likes', 'user']