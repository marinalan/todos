from django.urls import path

from .views import index, todo_detail

urlpatterns = [
    path('index', index),
    path('todo/<int:todo_id>', todo_detail),
]

