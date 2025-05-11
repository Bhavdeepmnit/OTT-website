from django import forms
from django.core.exceptions import ValidationError
from .models import User

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
