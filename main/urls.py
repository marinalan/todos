from django.urls import path

from .views import index, todo_detail, TodoCreateView, TodoUpdateView

urlpatterns = [
    path('', index, name='index'),
    path('todo/<int:todo_id>/', todo_detail, name='todo_detail'),
    path('todo/', TodoCreateView.as_view(), name='todo_create'),
    path('todo/<int:pk>/update/', TodoUpdateView.as_view(), name='todo_update'),
]

