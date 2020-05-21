from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm

def register2(request):
    #form = UserCreationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'New account has been creater for the user {username}')
            return redirect('blog-home')
    else:
        form = UserRegistrationForm()
    return render(request, 'user2/register.html', {'form': form})
