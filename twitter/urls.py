"""twitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from core import views
from django.conf.urls import include, url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.splash, name='splash'),
    path('signup', views.signup, name='signup'),
    path('profile/<str:id>', views.profile, name='profile'),
    path('hashtag/<str:tag>', views.hashtag, name='hashtag'),
    path('home', views.home, name='home'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('add_tweet', views.add_tweet, name="add_tweet"),
    path('delete', views.delete_tweet, name='delete'),
    path('like', views.like, name='like'),
]
