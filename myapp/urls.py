from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    # path('dashboard/', TemplateView.as_view(template_name='registration/dash.html'), name='dashboard'),
    # path('changepass/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html', success_url ='/myapp/changepassDone/'),  name='changepass'),
    # path('changepassDone/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='changepassDone'),

    path('login/', views.StudentLoginView.as_view(), name='login'),
    path('logout/', views.StudentLogoutView.as_view(), name='logout'),
    path('dashboard/', TemplateView.as_view(template_name='registration/dash.html'), name='dashboard'),
    path('changepass/', views.StudentPassChangeView.as_view(),  name='changepass'),
    path('changepassDone/', views.StudentPassChangedoneView.as_view(), name='changepassDone'),
    path('passwordSet/', views.StudentPassSetView.as_view(), name='passwordSet'),
    

]