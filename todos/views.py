from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task, Status
from .forms import TaskForm

# 1. タスク一覧を表示するView
class TaskListView(ListView):
    model = Task
    template_name = 'todos/task_list.html'
    context_object_name = 'tasks'

# 2. タスクを作成するView
class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'todos/task_form.html'
    success_url = reverse_lazy('task_list')

# 3. タスクを更新するView（ここがエラーの原因でした！）
class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'todos/task_form.html'
    success_url = reverse_lazy('task_list')

# 4. ステータス切り替えView（これは関数ベースのままでOKです）
def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    new_status = Status.objects.exclude(id=task.status.id).first()
    if new_status:
        task.status = new_status
        task.save()
    return redirect('task_list')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'todos/task_confirm_delete.html'
    success_url = reverse_lazy('task_list')  # 削除成功後は一覧へ