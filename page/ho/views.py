from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'ho/home.html', {'title':'Something'})
