# todo_project/urls.py

from django.contrib import admin
from django.urls import path, include  # include をインポートします！

urlpatterns = [
    path('admin/', admin.site.urls),
    # --- ここから追加 ---
    # 'todo/' で始まるリクエストを、todos/urls.py に渡す
    path('todo/', include('todos.urls')), 
    # --- ここまで追加 ---
]
