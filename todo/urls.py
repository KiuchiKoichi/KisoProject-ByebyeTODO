from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = [
    path('create/', views.create_group, name='create_group'),
    path('update/', views.update_group, name='update_group'),
    path('delete/', views.delete_group, name='delete_group'),
    path('<int:group_id>/', views.todolist, name='todolist'),
    path('<int:group_id>/create/', views.create_task, name='create_task'),
    path('<int:group_id>/update/', views.update_task, name='update_task'),
    path('<int:group_id>/delete/', views.delete_task, name='delete_task'),
]
