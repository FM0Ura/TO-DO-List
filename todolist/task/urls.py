from django.urls import path
from . import views

urlpatterns = [
    path('helloworld/', views.helloWorld),
    path('', views.taskList, name='task-list'),
    path('yourname/<str:name>', views.yourname, name='your-name'),
]