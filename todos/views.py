from django.shortcuts import render, get_object_or_404, redirect
from .models import Task, Status

# 一覧表示View
def task_list_view(request):
    # すべてのタスクを取得
    tasks = Task.objects.all()
    # 辞書形式でTemplateに渡すデータを準備
    context = {'tasks': tasks}
    # render(リクエスト, テンプレートのパス, 渡すデータ)
    return render(request, 'todos/task_list.html', context)

# ステータス切り替えView
def toggle_task_status(request, task_id):
    # 指定されたIDのタスクを取得（なければ404エラー）
    task = get_object_or_404(Task, id=task_id)
    
    # 簡易的な切り替えロジック：
    # 「未完了」なら「完了」に、「完了」なら「未完了」にする（Statusモデルにデータがある前提）
    # ※ここでは動作確認のため、最初に見つかった別のステータスに入れ替えます
    new_status = Status.objects.exclude(id=task.status.id).first()
    if new_status:
        task.status = new_status
        task.save() # データベースを更新！

    # 処理が終わったら一覧画面に戻る
    return redirect('task_list')