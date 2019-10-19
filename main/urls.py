from django.urls import path

from .views import index, todo_detail, todo_create

urlpatterns = [
    path('index', index, name='index'),
    path('todo/<int:todo_id>', todo_detail, name='todo_detail'),
    path('todo/', todo_create, name='todo_create'),
]

