from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'h4/h4home.html', {'title':'Something new'})
