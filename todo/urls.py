from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.todolist, name='todolist'),
    path('add/', views.add, name='add'),
    path('delete_modify/', views.delete_modify, name='delete_modify'),
]
