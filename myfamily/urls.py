"""myfamily URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views

from django.conf import settings


urlpatterns = [
    path('register/', user_views.register, name='register'),
    path('delete-user/', user_views.del_user, name='delete-user'),
    path('profile/', user_views.profile, name='profile'),
    path('about/', user_views.about, name='about'),
    path('top50/', user_views.top50, name='top50'),
    path('password/', user_views.change_password, name='change-password'),
    path('delete-all-words/', user_views.delete_words, name='delete-all-words'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', include('cart.urls', namespace='cart')),
]

if settings.DEBUG:
    urlpatterns.append(path('admin/', admin.site.urls))
