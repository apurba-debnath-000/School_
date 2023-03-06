from django.urls import path, register_converter
from . import views, converters
from .views import *

register_converter(converters.FourDigitYearConverter,'yyyy')
urlpatterns =[
    path('', views.home, name="home"),
    path('session/<yyyy:year>/', views.year, name="year"),
    path('profile/', views.userprofile, name="profile"),
    path('teacher_reg/',views.teacherReg, name='teacher_reg'),
    path('login/',views.login, name='login'),
    path('logout/',views.user_logout, name='logout'),
    path('change_pass/',views.changePass, name='change_pass'),
    path('userdetails/<int:id>',views.userdetails, name='userdetails'),
]