from django.shortcuts import render, get_object_or_404, redirect
from .models import Task, Status
from .forms import TaskForm  # これを忘れずに追加してください！
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskForm

# タスク一覧を表示するView
class TaskListView(ListView):
    model = Task  # どのモデルのデータを使うか
    template_name = 'todos/task_list.html'  # 使用するテンプレート
    context_object_name = 'tasks'  # テンプレート内で使う変数名

# タスクを作成するView
class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'todos/task_form.html'
    # 保存に成功した後の移動先（URLの名前を指定）
    success_url = reverse_lazy('task_list')

# 登録画面View
def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'todos/task_form.html', {'form': form})

# 一覧表示View（名前を task_list に修正しました）
def task_list(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'todos/task_list.html', context)

# ステータス切り替えView
def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    new_status = Status.objects.exclude(id=task.status.id).first()
    if new_status:
        task.status = new_status
        task.save()
    return redirect('task_list')