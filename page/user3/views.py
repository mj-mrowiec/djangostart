from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your views here.

def register(request):
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print('POST request raised')
        if form.is_valid():
            print('save it into the db')
    else:
        form = UserCreationForm()
    return render(request, 'user3/register.html', {'form':form})