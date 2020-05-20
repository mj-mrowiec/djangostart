from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print('Alpha')
        print(str(form.is_valid()))
        if form.is_valid():
            username = form.cleaned_data.get('username')
            print('Betta')
            messages.success(request, f'Accout Created for {username}!')
            return redirect('blog-home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form':form})

#messages.debug
#messages.success
#messages.warning
#messages.error