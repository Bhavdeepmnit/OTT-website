from django import forms
from django.core.exceptions import ValidationError
from .models import User

class SignupForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_mail(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email address is already in use.")
        return email
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password)<8:
            raise ValidationError("Password must be at least 8 characters long.")
        return password