from django import forms
from .models import Pupils

class ContactForm(forms.Form):
    name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))
    phone = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))
    
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    msg = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))

class ContactFromDetails(forms.ModelForm):
    
    class Meta:
        model = Pupils
        fields = '__all__'
        widgets = {
            'p_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your name'}),
            'p_email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter your email'}),
            'p_roll': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Enter your roll'}),
            'p_course': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your course'}),
            'p_password': forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter your password'}),
                   
                   }
        labels = {'p_name':'Name', 'p_email':'Email', 'p_roll':'Roll', 'p_course':'Course', 'p_password':'Password'}
