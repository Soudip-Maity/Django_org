from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import post_model

class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField()
    class meta():
        model=User
        fields = ('username', 'email', 'password1','password2')


class postform(forms.ModelForm):
    class Meta:
        model = post_model
        fields = ['text', 'photo']
        