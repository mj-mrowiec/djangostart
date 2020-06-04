from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreated
# Create your views here.

def home(request):
    if request.method == 'POST':
        form = UserCreated(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Something like created')
            return redirect('blog-home')
    else:
        form = UserCreated()

    return render(request, 'user2/register.html', {'form': form})
