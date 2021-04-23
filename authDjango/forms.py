from django import forms
from .models import UserProfileInfo


class UserProfileInfoForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'fist name'
    }))
    
    password = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'type':'password',
        'placeholder':'Password'
    }))
    
    email = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Email'
    }))
  
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'fist name'
    }))
    
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'last name'
    }))


    password_validation = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'type':'password',
        'placeholder':'Re-enter Password'
    }))

    portfolio_site = forms.URLField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Portfolio Site'
    }))

    profile_pic = forms.ImageField()

    class Meta:
        model = UserProfileInfo
        fields = ('username','password','password_validation')

    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=45, label='Username',widget=forms.TextInput(attrs={
        'class':'form-control',
        'type':'text',
        'placeholder':'Username'
    }))
    password = forms.CharField(max_length=45, label='Password', widget=forms.TextInput(attrs={
        'class':'form-control',
        'type':'password',
        'placeholder':'Password'
    }))
