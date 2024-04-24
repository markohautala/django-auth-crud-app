from django.urls import path
from .views import TaskList, TaskDetail

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'), # This is the URL that will be used to access the view
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
]  