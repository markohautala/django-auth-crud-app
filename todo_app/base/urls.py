from django.urls import path
from .views import TaskList, TaskDetail, CreateTask, UpdateTask, DeleteTask, EnhancedLoginView

# These are the URLs that will be used to access the views
urlpatterns = [
    path('login/', EnhancedLoginView.as_view(), name='login'),
    path('', TaskList.as_view(), name='tasks'), 
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'), 
    path('create-task/', CreateTask.as_view(), name='create-task'), 
    path('task-update/<int:pk>/', UpdateTask.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', DeleteTask.as_view(), name='task-delete'),
]  