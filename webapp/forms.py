from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from . models import Record



class CreateUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class CreateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        exclude = ['creation_date']
        
class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        exclude = ['creation_date']
     
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())