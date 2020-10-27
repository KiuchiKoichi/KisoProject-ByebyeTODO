from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = [
    path('<int:group_id>/', views.index, name='index'),
    path('<int:group_id>/add/', views.add_task, name='add'),
    path('<int:group_id>/delete/', views.delete_task, name='delete'),
    path('<int:group_id>/modify/', views.modify_task, name='modify'),
]
