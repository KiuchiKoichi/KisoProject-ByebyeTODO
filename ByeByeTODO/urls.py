
from django.urls import path
from . import views


app_name = 'ByeByeTODO'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
]
