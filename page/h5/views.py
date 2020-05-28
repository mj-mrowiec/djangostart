from django.shortcuts import render

# Create your views here.

def home_view(requests):

    return render(requests, 'h5/home.html', {'title':'My title'})
