from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField, PasswordChangeForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import  password_validation


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'class':'form-control', 'autofocus':True}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password", 'class':'form-control'}),
    )

class StudentPassChangeForm(PasswordChangeForm):

    old_password = forms.CharField(
        label=_("Old password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={'class':'form-control',"autocomplete": "current-password", "autofocus": True}
        ),
    )
    new_password1 = forms.CharField(
            label=_("New password"),
            widget=forms.PasswordInput(attrs={"autocomplete": "new-password" , 'class':'form-control'}),
            strip=False,
            help_text=password_validation.password_validators_help_text_html(),
        )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password" , 'class':'form-control'}),
    )
