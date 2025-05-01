from django.forms import  CharField, TextInput, PasswordInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegisterForm(UserCreationForm):
    username = CharField(min_length=4, max_length=10, required=True,
                         widget=TextInput(attrs={'class': 'form-control'}))
    email = CharField(required=True, widget=TextInput(attrs={'class': 'form-control'}))
    password1 = CharField(required=True,
                          widget=PasswordInput(attrs={'class': 'form-control'}))
    password2 = CharField(required=True,
                          widget=PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = CharField(min_length=4, max_length=10, required=True,
                         widget=TextInput(attrs={'class': 'form-control'}))
    password = CharField(required=True,
                         widget=PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'password']
