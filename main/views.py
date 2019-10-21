from datetime import datetime

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, UpdateView, ListView, DetailView, DeleteView, View
)

#from django.http import HttpResponse, Http404

from .models import Todo
from .forms import TodoForm

class IndexView(ListView):
    queryset = Todo.objects.all()
    template_name = 'main/index.html'
    context_object_name = 'todos'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['today'] =  datetime.now()
        ctx['app_name'] = "Super Todos"
        return ctx


class TodoDetailsView(DetailView):
    model = Todo

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

class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy('index')

class TodoJsonView(View):
    def get(self, request, *args, **kwargs):
        todos = Todo.objects.filter(done=True).values()
        return JsonResponse({'todos': list(todos)})
