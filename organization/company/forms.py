from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import post_model

class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField(required=True)
    class meta():
        model=User
        fields = ('username', 'email', 'password1','password2')

class AdminRegistrationForm(UserCreationForm):
    email=forms.EmailField(required=True)
    is_superuser = forms.BooleanField(required=True, label="Superuser")

    class Meta:
        model=User
        fields = ('username', 'email', 'password1','password2','is_superuser')


class postform(forms.ModelForm):
    class Meta:
        model = post_model
        fields = ['text', 'photo']
        