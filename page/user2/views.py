from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm

def register2(request):
    #form = UserCreationForm()
    form = UserRegistrationForm()
    return render(request, 'user2/register.html', {'form': form})
