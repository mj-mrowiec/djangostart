from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def register2(request):
    form = UserCreationForm()
    return render(request, 'user2/register.html', {'form': form})
