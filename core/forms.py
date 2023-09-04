from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms 
from .models import Blog


class SignUpForm(UserCreationForm):
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        widgets={
            'username': forms.TextInput(attrs={
                'class':'form-control'
            }),
            'first_name':forms.TextInput(attrs={
                'class':'form-control',
            }),
            'last_name':forms.TextInput(attrs={
                'class':'form-control'
            }),
            'email':forms.EmailInput(attrs={
                'class':'form-control'
            })
        }



class EditProfileForm(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','date_joined','last_login']


class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=['title','description']
