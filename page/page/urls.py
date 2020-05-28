"""page URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as user_views 
from user2 import views as user2_views
from user3 import views as user3_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('h5/', include('h5.urls')),
    path('register/', user_views.register, name = 'register'),
    path('', include('blog.urls')),
    path('about/', include('about.urls')),
    path('register2/', user2_views.register2, name = 'register2'),
    path('register3/', user3_views.register ,name='register3'),
]
