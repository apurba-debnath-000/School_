from django.urls import path
from . import views
from .views import homeEnroll

urlpatterns =[

    path('homeEnroll/', views.homeEnroll, name="homeEnroll")
]