from django.shortcuts import render
from django.views.generic.base import TemplateView

from django import forms
from .forms import LoginPageForm
from django.contrib.auth.models import User
# Create your views here.
class ProfileTemplateView(TemplateView):
    template_name='registration/profile.html'

class LogoutTemplateView(TemplateView):
    template_name='registration/logout.html'