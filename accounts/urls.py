from django.urls import path
from . import views

urlpatterns = [

    path('profile/', views.ProfileTemplateView.as_view(), name='profile'),
    path('logout/', views.LogoutTemplateView.as_view(), name='logout'),




]
