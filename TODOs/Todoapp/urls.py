from django.urls import path
from Todoapp import views

urlpatterns = [
    path('todolist/', views.TodolistaApi, name='todolist'),
    path('todolist/<int:pk>', views.TodolistaApi, name='todolist-detail'),
]