from django.urls import path
from .views import relHome


urlpatterns = [
    path('', relHome, name="relhome")
]