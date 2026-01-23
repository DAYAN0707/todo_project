from django.urls import path
from .views import TaskListView, TaskCreateView, toggle_task 

urlpatterns = [
    path('list/', TaskListView.as_view(), name='task_list'),
    path('create/', TaskCreateView.as_view(), name='task_create'),
    path('toggle/<int:task_id>/', toggle_task, name='toggle_task'),
]