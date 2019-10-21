from datetime import datetime

from django.contrib import messages
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404

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

def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "The todo was created successfully.")
            return redirect('index')
        return render(request, 'main/todo.html', {'form': form})
    return render(request, 'main/todo.html', {'form': TodoForm()})

def todo_update(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, "The todo was updated successfully.")
            return redirect('index')
        return render(request, 'main/todo.html', {'form': form})
    return render(request, 'main/todo.html', {'form': TodoForm(instance=todo)})

