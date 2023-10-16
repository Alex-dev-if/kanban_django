from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('create-task/', views.create_task, name='create_task'),
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
    path('task/<int:task_id>/delete/', views.task_delete, name='task_delete'),
    path('task/<int:task_id>/edit/', views.task_edit, name='task_edit'),
    path('update_task_status/<int:task_id>/<str:new_status>/', views.update_status, name='update_task_status'),
    path('dashboard/', views.dashboard, name='dashboard'),

]