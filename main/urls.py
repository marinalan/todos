from django.urls import path

from .views import (
    TodoCreateView, TodoUpdateView, IndexView, TodoDetailsView,
    TodoDeleteView,TodoJsonView
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('todo/<int:pk>/', TodoDetailsView.as_view(), name='todo_detail'),
    path('todo/', TodoCreateView.as_view(), name='todo_create'),
    path('todo/<int:pk>/update/', TodoUpdateView.as_view(), name='todo_update'),
    path('todo/<int:pk>/delete/', TodoDeleteView.as_view(), name='todo_delete'),
    path('todo/json/', TodoJsonView.as_view(), name='todo_json'),
]

