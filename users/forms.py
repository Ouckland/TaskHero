from django import forms
from django.contrib.auth import get_user_model, authenticate 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=255,  widget=forms.TextInput(attrs={'placeholder' : 'First name',}))
    last_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder' : 'Last name',}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder' : 'Email',}))
    username = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder' : 'Username',}))
    password1 = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'email', 'username',
        ]

class LoginForm(forms.Form):
    username = forms.CharField(required=True, max_length=255, widget=forms.TextInput())
    password = forms.CharField(required=True, max_length=255, widget=forms.PasswordInput())
