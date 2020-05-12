from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'h1/h1home.html', {'title':'Something'})
