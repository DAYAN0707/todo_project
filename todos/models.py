from django.db import models

# 1. タスクの状態を管理するモデル（例：未完了、進行中、完了）
class Status(models.Model):
    name = models.CharField(max_length=50, verbose_name="ステータス名")

    def __str__(self):
        return self.name

# 2. タスク本体を管理するモデル
class Task(models.Model):
    title = models.CharField(max_length=100, verbose_name="タスク名")
    description = models.TextField(blank=True, verbose_name="詳細説明")
    # Statusモデルと紐付け（1つのステータスに複数のタスクが紐付く「1対多」の関係）
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name="状態")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")

    def __str__(self):
        return self.title