from django.urls import path
from .views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView, toggle_task 

urlpatterns = [
    path('list/', TaskListView.as_view(), name='task_list'),
    path('create/', TaskCreateView.as_view(), name='task_create'),
    # 更新用のパス
    path('update/<int:pk>/', TaskUpdateView.as_view(), name='task_update'),
    path('toggle/<int:task_id>/', toggle_task, name='toggle_task'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='task_delete'),
]