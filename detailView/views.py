from django.shortcuts import render, HttpResponse
from .models import *
from .forms import ContactForm, ContactFromDetails
# Create your views here.
from django.views.generic.base import TemplateView, RedirectView

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django import forms
class NewYoutubeRedirectView(RedirectView):
    pattern_name = 'mindex'
    permanent = True
    query_string = False

    def get_redirect_url(self, *args, **kwargs): 
        print(kwargs)
        return super().get_redirect_url(*args, **kwargs)

class ListPupils(ListView):
    model = Pupils
    #here context is modelname_list / object_list
    #template_name_suffix = '_get'
    #ordering = ['id']
    template_name = 'detailView/pupils.html'
    context_object_name = 'students'
    # def get_queryset(self):
    #     return Pupils.objects.filter(p_course='Python')
    
    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context['freshers'] = Pupils.objects.all().order_by('p_name')
    #     return context
    
    # def get_template_names(self):
    #     if self.request.COOKIES['user'] == 'sonam':
    #         template_name = 'detailView/sonam.html'
    #     else:
    #         template_name = self.template_name
    #     return [template_name]


class PupilsDetailView(DetailView):
    model = Pupils
    template_name = 'detailView/pupils_del.html'
    context_object_name = 'stu'

class StdFormView(FormView):
   form_class = ContactForm
   template_name = 'formView/index.html'
   success_url = '/detailView/thankyou/'

   def form_valid(self, form):
       print('Name:--',form.cleaned_data['name'])
       print('Phone:--',form.cleaned_data['phone'])
       print('Email:--',form.cleaned_data['email'])
       print('Message:--',form.cleaned_data['msg'])
    #  return super().form_valid(form)
       return HttpResponse('Message Sent')


class ThanksTemplateView(TemplateView):
    template_name='formView/thank.html'

#Createview
# class CreateViewPupil(CreateView):
#     model = Pupils
#     fields = ['p_name', 'p_email', 'p_roll','p_course', 'p_password']
#     template_name = 'createView/index.html'
#     #success_url = '/detailView/thankyou/'
#     #get absolute url:

#     def get_form(self ):
#         form = super().get_form()
#         form.fields['p_name'].label = 'Name'
#         form.fields['p_email'].label = 'Email'
#         form.fields['p_roll'].label = 'Your roll'
#         form.fields['p_course'].label = 'Course'
#         form.fields['p_password'].label = 'Password'


#         form.fields['p_name'].widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your name'})
#         form.fields['p_email'].widget = forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter your email'})
#         form.fields['p_roll'].widget = forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Enter your roll'})
#         form.fields['p_course'].widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your course'})
#         form.fields['p_password'].widget = forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter your password'})
#         return form


class CreateViewPupil(CreateView):
    form_class = ContactFromDetails
    template_name = 'createView/index.html'
    #success_url = '/detailView/thankyou/'


class SigleDataDetail(DetailView):
    model = Pupils
    template_name = 'createView/pupils_details.html'
    context_object_name= 'stu'

    # success_url = '/detailView/thankyou/'
    #get absolute url:


class SingleDataUpdate(UpdateView):
    model = Pupils
    fields = ['p_name', 'p_email', 'p_roll','p_course', 'p_password']
    
    template_name = 'createView/update.html'
    success_url = '/detailView/thankyou/'

    def get_form(self ):
        form = super().get_form()
        form.fields['p_name'].label = 'Name'
        form.fields['p_email'].label = 'Email'
        form.fields['p_roll'].label = 'Your roll'
        form.fields['p_course'].label = 'Course'
        form.fields['p_password'].label = 'Password'


        form.fields['p_name'].widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your name'})
        form.fields['p_email'].widget = forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter your email'})
        form.fields['p_roll'].widget = forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Enter your roll'})
        form.fields['p_course'].widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your course'})
        form.fields['p_password'].widget = forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter your password'})
        return form


class SingleDataDel(DeleteView):
    model = Pupils
    template_name = 'deleteView/delete.html'
    context_object_name= 'pupils'
    success_url = '/detailView/pupilslist/'
    
    