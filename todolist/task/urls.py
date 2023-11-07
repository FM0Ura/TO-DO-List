from django.urls import path
from . import views

urlpatterns = [
    path('', views.helloWorld),
    path('task-list/', views.taskList, name="task-list"),
    path('yourname/<str:name>', views.yourname, name="yourname"),
]