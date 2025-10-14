from django.urls import path
from . import views

app_name = 'TaskHero'
urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add/task/', views.add_task, name='add_task'),
    path('task/detail/<int:task_id>/', views.task_detail, name='task_detail'),
    path('edit/task/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete/task/<int:task_id>/', views.delete_task, name='confirm_delete'),

]
