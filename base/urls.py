from django.urls import path
from .views import TaskList, TaskDetail, CreateTask, UpdateTask, DeleteTask, EnhancedLoginView, RegisterUserPage, HomeView
from django.contrib.auth.views import LogoutView

# These are the URLs that will be used to access the views
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', EnhancedLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterUserPage.as_view(), name='register'),

    path('tasks/', TaskList.as_view(), name='tasks'), 
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'), 
    path('create-task/', CreateTask.as_view(), name='create-task'), 
    path('task-update/<int:pk>/', UpdateTask.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', DeleteTask.as_view(), name='task-delete'),
]  