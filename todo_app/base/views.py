from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task

# Create your views here.
class TaskList(ListView):
    model = Task
    context_object_name = 'todo_tasks'

class TaskDetail(DetailView):
    model = Task
    context_object_name = 'todo_task'
    template_name = 'base/single_task.html'

class CreateTask(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class UpdateTask(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class DeleteTask(DeleteView):
    model = Task
    context_object_name = 'todo_tasks'
    success_url = reverse_lazy('tasks')
    template_name = 'base/task_confirm_delete.html'