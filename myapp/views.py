from django.shortcuts import render

from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView

from .forms import LoginForm, StudentPassChangeForm


class StudentLoginView(LoginView):
    template_name='registration/login.html'
    authentication_form = LoginForm

class StudentLogoutView(LogoutView):
    template_name='registration/logout.html'

class StudentPassChangeView(PasswordChangeView):

    form_class = StudentPassChangeForm
    template_name='registration/password_change.html'
    success_url ='/myapp/changepassDone/'


class StudentPassChangedoneView(PasswordChangeDoneView):
    template_name='registration/password_change_done.html'


class StudentPassSetView(PasswordResetView):
    template_name='registration/pass_reset.html'


