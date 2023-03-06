from django import forms
from django.core import validators
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm, PasswordChangeForm



# class StudentRegForm(forms.Form):
#     std_id =forms.CharField(error_messages={'required': 'Please enter your student id'}, required=False, min_length=3)
#     name = name = forms.CharField(error_messages={'required': 'Please enter your name'}, required=False,min_length=3)
#     email =forms.EmailField(error_messages={'required': 'Please enter your email'}, required=False, min_length=16)

class StudentRegForm(forms.ModelForm):
    #password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Student
        fields = ['std_id', 'name', 'email', 'password' ]
        labels = {'std_id':'Student id:','name':'Your Name', 'email':'Your Email','password':'Your Password',}
        help_text = {'name':'Enter your full name'}
        error_messages={'name':{'required':'Enter your full name'}, 'password':{'required':'Enter a 6 digit password'}}
        widgets = {
            'std_id':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your student id'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter your password'}),
            'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your name'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter your email'}),
            
        }


class TeacherRegForm(UserCreationForm):
    password2 = forms.CharField(

        label='Confirm Password', 
        error_messages={'required': 'Please enter your password again.'}, 
        widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter password again.'}
        
        ))
    password1 = forms.CharField(

        label='Password', 
        error_messages={'required': 'Please enter your password'}, 
        widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter 8 digit password.'}
        
        ))
    first_name = forms.CharField(
        label='First name',
        required=True,
        error_messages={'required': 'Please enter first name'},
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your first name'}
     ))
    last_name = forms.CharField(
        label='Last name',
        required=True,
        error_messages={'required': 'Please enter last name'},
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your last name'}
     ))
    email = forms.EmailField(
        label='Email',
        required=True,
        error_messages={'required': 'Please enter email.'},
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your email.'}
     ))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

        labels = {'email':'Email'}
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your user name.'}),
            'first_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your first name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your last name'}),
            'email':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your last email'}),
        }
        error_messages={
            'username':{'required':'Enter your username.'},
            'first_name':{'required':'Enter your first_name.'},
            'last_name':{'required':'Enter your last_name.'},
            'email':{'required':'Enter your email.'},
        
        
        }

class LoginFrom(AuthenticationForm):
    password = forms.CharField(

        label='Password', 
        error_messages={'required': 'Please enter your password'}, 
        widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter password '}
        
        ))
    username = forms.CharField(
        label='User name',
        required=True,
        error_messages={'required': 'Please enter user name'},
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your user name'}
     ))
   
   
class ChangeUserPass(PasswordChangeForm):
    old_password = forms.CharField(

        label='Password', 
        error_messages={'required': 'Please enter your old password'}, 
        widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter old password '}
        
        ))
    new_password1 = forms.CharField(

        label='Password', 
        error_messages={'required': 'Please enter your new password'}, 
        widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter new password '}
        
        ))
    new_password2 = forms.CharField(

        label='Password', 
        error_messages={'required': 'Please enter your new password again'}, 
        widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter new password again'}
        
        ))


class EditProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email':'Email'}
        widgets={
                'username':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your user name.'}),
                'first_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your first name'}),
                'last_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your last name'}),
                'email':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your last email'}),
            }
        error_messages={
                'username':{'required':'Enter your username.'},
                'first_name':{'required':'Enter your first_name.'},
                'last_name':{'required':'Enter your last_name.'},
                'email':{'required':'Enter your email.'},
            
            
            }

class EditAdminProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = '__all__'
        exclude = ['password']
        labels = {'email':'Email'}
        widgets={
                'username':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your user name.'}),
                'first_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your first name'}),
                'last_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your last name'}),
                'email':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your last email'}),
                
        
        
            }
        error_messages={
                'username':{'required':'Enter your username.'},
                'first_name':{'required':'Enter your first_name.'},
                'last_name':{'required':'Enter your last_name.'},
                'email':{'required':'Enter your email.'},
            
            
            }
