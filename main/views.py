from datetime import datetime

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

#from django.http import HttpResponse, Http404

from .models import Todo
from .forms import TodoForm

def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos,    
        'today': datetime.now(),
        'app_name': "Super Todos"
    }
    return render(request, 'main/index.html', context=context)
    #template = loader.get_template('main/index.html')
    #return HttpResponse(template.render(context, request))

def todo_detail(request, todo_id):
  todo = get_object_or_404(Todo, pk=todo_id)

  context = {
    'todo': todo
  }
  return render(request, 'main/todo_detail.html', context=context)
  # try:
  #   todo = Todo.objects.get(pk=todo_id)
  #   context = {
  #     'todo': todo
  #   }
  #   return render(request, 'main/todo_detail.html', context=context)
  # except Todo.DoesNotExist:
  #   raise Http404("Todo with id: {} does not exist.".format(todo_id))

class TodoCreateView(SuccessMessageMixin, CreateView):
    model = Todo
    form_class = TodoForm
    template_name = 'main/todo.html'
    success_url = reverse_lazy('index')
    success_message = 'Todo has been created successfully.'


class TodoUpdateView(SuccessMessageMixin, UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = 'main/todo.html'
    success_url = reverse_lazy('index')
    success_message = 'Todo has been updated successfully.'
