from django.urls import path
from . import views

urlpatterns = [
    # ブラウザで見る一覧画面
    path('list/', views.task_list_view, name='task_list'),
    # ステータスを切り替えるための処理用URL（画面は持たず、処理後にリダイレクト）
    path('toggle/<int:task_id>/', views.toggle_task_status, name='toggle_task'),
]