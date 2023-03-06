from django.urls import path

from . import views
from .views import set_session


urlpatterns =[
    path('setSession/', views.set_session, name="set_session"),
    path('getSession/', views.get_session, name="get_session"),
    path('delSession/', views.del_session, name="del_session"),

]