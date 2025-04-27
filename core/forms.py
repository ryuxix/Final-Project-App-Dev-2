from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from .models import Routine

class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username','email','password1','password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
    

class RoutineForm(forms.ModelForm):
    class Meta:
        model = Routine
        fields = ['title', 'content', 'game']
        widgets = {
            'game': forms.HiddenInput()
        }