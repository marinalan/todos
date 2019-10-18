from datetime import datetime
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Todo

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
