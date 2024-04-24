from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task

# Create your views here.
class TaskList(ListView):
    model = Task
    context_object_name = 'todo_tasks'

class TaskDetail(DetailView):
    model = Task
    context_object_name = 'todo_task'
    template_name = 'base/single_task.html'