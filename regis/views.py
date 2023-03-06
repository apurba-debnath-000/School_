from django.shortcuts import render, HttpResponseRedirect
from . import forms
from .forms import StudentRegForm, TeacherRegForm, LoginFrom, ChangeUserPass, EditProfileForm, EditAdminProfileForm
from .models import Student
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.contrib.auth import login as auth_login
# Create your views here.

def home(request):
    if request.method == 'POST':
        form = StudentRegForm(request.POST)
        if form.is_valid():
            nm = form.cleaned_data.get('name') 
            sid = form.cleaned_data.get('std_id')
            em = form.cleaned_data.get('email')
            pw = form.cleaned_data.get('password')
            data = Student(std_id=sid, name=nm, email=em, password=pw)
            data.save()
            form = StudentRegForm()
            #messages.add_message(request, messages.SUCCESS, "Your account has been created!!! ")
            messages.info(request,"Now you can login!!!")
            messages.debug(request,"this is debug")
            print(messages.get_level(request))
            messages.set_level(request, messages.DEBUG)
            messages.debug(request, "This is new debug.")
            print(messages.get_level(request))
            
    else:
        form = StudentRegForm()
    return render(request, 'home/index.html', {'form':form})


def teacherReg(request):
    if request.method == 'POST':
        fm = TeacherRegForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.add_message(request, messages.SUCCESS, 'User created successfully!! ')
            fm = TeacherRegForm()

    else:
        fm = TeacherRegForm()
    return render(request, 'account/teacher_reg.html', {'form':fm})

#login
def login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = LoginFrom(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                #now we have to authenticate this field:
                user = authenticate(username=uname, password=upass) #this authenticate function return user object after match
                if user is not None:
                    auth_login(request, user)
                    messages.success(request, "Loged in successfully!!")
                    return HttpResponseRedirect('/profile/')

                else:
                    messages.info(request, "Username or Password incorrect!! Try again")
                
        else:
            fm = LoginFrom()
        return render(request,'account/login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/profile/')

def year(request, year):
    std={'yr':year}
    return render(request,'home/year.html', std)

def userprofile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            if request.user.is_superuser == True:
                fm = EditAdminProfileForm(request.POST,instance=request.user)
                users = User.objects.all()
            else:
                fm = EditProfileForm(request.POST, instance=request.user)
            if fm.is_valid():
                fm.save()
                messages.success(request, "Profile updated successfully!! ")
        #get
        else:
            if request.user.is_superuser == True:
                fm = EditAdminProfileForm(instance=request.user)
                users =   None
            else:
                fm = EditProfileForm(instance=request.user)
        return render(request, 'home/profile.html', {'user':request.user, 'form':fm, 'users':users})
    else:
        return HttpResponseRedirect('/login/')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def userdetails(request, id):
    if request.user.is_authenticated:
        pi = User.objects.get(pk=id)
        fm = EditAdminProfileForm(instance=pi)
        return render(request, 'home/user_detail.html', {'form':fm})
    else:
        return HttpResponseRedirect('/login/')


def changePass(request):
    #SetPasswordForm -- for without old password. rest of the work as it is.
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = ChangeUserPass(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request, 'Password changed successfully!!')
                return HttpResponseRedirect('/profile/')
        else:
            fm = ChangeUserPass(user=request.user)
        return render(request, 'home/change_pass.html', {'fm':fm})
    else:
        return HttpResponseRedirect('/login/')
