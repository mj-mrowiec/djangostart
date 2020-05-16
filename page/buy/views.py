from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'buy/buyhome.html', {'title':'My new title'})