from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
    'author': 'MatM',
    'title': 'Blog Post 1',
    'content': 'Something about the specific function that Im planning to learn',
    'date': '01-05-2019'
    },
    {
     'author':'MatW',
     'title':'Blog post 2',
     'content':'other content',
     'date': '01-05-2020'   
    },
    {
     'author':'MatX',
     'title':'Blog post 3',
     'content':'other content',
     'date': '05-05-2020'   
    }
]


def home(request):
    context = {
        'posts': posts
    }
    #return HttpResponse('<h1>Blog Home</h1>')
    return render(request, 'blog/home.html', context)

def about(request):
    #return HttpResponse('<h1>Blog About</h1>')
    return render(request, 'blog/about.html', {'title': 'Something'})