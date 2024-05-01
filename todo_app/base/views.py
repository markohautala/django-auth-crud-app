from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth.forms import UserCreationForm # This is the form that will be used to create a new user
from django.contrib.auth import login # This is the method that will be used to log in the user

from .models import Task

# LoginView in top because it is a gatekeeper for users to access the app
class EnhancedLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True # Redirects user to tasks page if already logged in

    def get_success_url(self):
        return reverse_lazy('tasks') # Redirects user to tasks page after successful login
    
class RegisterUserPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True # Redirects user to tasks page if already logged in
    success_url = reverse_lazy('tasks') # Redirects user to tasks page after successful registration

    def form_valid(self, form):
        user = form.save() # Saves the user to the database
        if user is not None:
            login(self.request, user) # Logs in the user after successful registration
        return super(RegisterUserPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterUserPage, self).get(*args, **kwargs)

# Create your views here.
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'todo_tasks'
    
    # this method is used to filter the tasks based on the specific user
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todo_tasks'] = context['todo_tasks'].filter(user=self.request.user)
        context['count'] = context['todo_tasks'].filter(complete=False).count()
        return context
    

class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'todo_task'
    template_name = 'base/single_task.html'

class CreateTask(LoginRequiredMixin, CreateView): 
    model = Task
    fields = ['title', 'description', 'complete'] # Fields that the user can fill out
    success_url = reverse_lazy('tasks')

    # this method is used to assign the user to the task
    def form_valid(self, form):
        form.instance.user = self.request.user # is the user that is currently logged in
        return super(CreateTask, self).form_valid(form)

class UpdateTask(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete'] # Fields that the user can update
    success_url = reverse_lazy('tasks')

class DeleteTask(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'todo_tasks'
    success_url = reverse_lazy('tasks')
    template_name = 'base/task_confirm_delete.html'