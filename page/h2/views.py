from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'h2/h2home.html', {'title':'Something'})
