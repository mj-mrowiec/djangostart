from django.shortcuts import render

# Create your views here.

def about(request):
    
    return render(request, 'about/home.html',{'title':'About me'})
