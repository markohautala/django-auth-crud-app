from django.urls import path
from . import views

urlpatterns = [
    path('', views.taskList, name='tasks'), # This is the URL that will be used to access the view
]