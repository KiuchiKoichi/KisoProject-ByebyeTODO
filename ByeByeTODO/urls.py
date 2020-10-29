from django.contrib import admin
from django.urls import path, include
from accounts.views import Top
from . import views


app_name = 'ByeByeTODO'

urlpatterns = [
    path('', views.index, name='index'),
    #path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
]
