
from django.urls import path, include
from . import views

app_name = 'account'
urlpatterns = [
    path('top/', views.TopView.as_viwe(), name='top')
]
