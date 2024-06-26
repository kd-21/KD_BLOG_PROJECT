from django import forms 
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from accounts.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['email', 'password1', 'password2']

class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)