from django.contrib import admin
from .models import Status, Task  # 自分の作ったモデルを読み込む

# 管理画面に表示されるように登録する
admin.site.register(Status)
admin.site.register(Task)