from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserCreated(UserCreationForm):
    email = forms.EmailField()

    class META:
        fields = ['username', 'email', 'password1', 'password2']