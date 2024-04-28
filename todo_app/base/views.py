from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin 

from .models import Task

# LoginView in top because it is a gatekeeper for users to access the app
class EnhancedLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True # Redirects user to tasks page if already logged in

    def get_success_url(self):
        return reverse_lazy('tasks') # Redirects user to tasks page after successful login


# Create your views here.
class TaskList(LoginRequiredMixin, ListView):
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