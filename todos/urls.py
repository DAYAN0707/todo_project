# todos/urls.py

from django.urls import path
from . import views # 現在のディレクトリのviews.pyから関数をインポート

# URLパターンを定義するリスト
urlpatterns = [
    # path('アクセスするURL/', 実行するView関数名, name='URLの識別名')
    path('hello/', views.hello_world_view, name='hello_world'),
    path('api/list/', views.json_data_view, name='api_list'),
]