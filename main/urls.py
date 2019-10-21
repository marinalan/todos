from django.urls import path

from .views import index, todo_detail, todo_create, todo_update

urlpatterns = [
    path('', index, name='index'),
    path('todo/<int:todo_id>/', todo_detail, name='todo_detail'),
    path('todo/', todo_create, name='todo_create'),
    path('todo/<int:todo_id>/update/', todo_update, name='todo_update'),
]

