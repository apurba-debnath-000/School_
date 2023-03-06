from django.urls import path
from . import views
from .views import *

urlpatterns =[
    path('', views.home, name="testhome"),
    path('qobjects/', views.q_objects, name="q_objects"),

]