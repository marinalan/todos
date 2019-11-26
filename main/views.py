from datetime import datetime

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, UpdateView, ListView, DetailView, DeleteView, View
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group, User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from pprint import pprint

#from django.http import HttpResponse, Http404

from .models import Todo
from .forms import ( TodoForm, SignupForm )

class IndexView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    queryset = Todo.objects.all()
    template_name = 'main/index.html'
    context_object_name = 'todos'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['today'] =  datetime.now()
        ctx['app_name'] = "Super Todos"
        return ctx


class TodoDetailsView(LoginRequiredMixin,DetailView):
    login_url = '/login/'
    model = Todo

class TodoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = '/login/'
    model = Todo
    form_class = TodoForm
    template_name = 'main/todo.html'
    success_url = reverse_lazy('index')
    success_message = 'Todo has been created successfully.'


class TodoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = '/login/'
    model = Todo
    form_class = TodoForm
    template_name = 'main/todo.html'
    success_url = reverse_lazy('index')
    success_message = 'Todo has been updated successfully.'

class TodoDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = Todo
    success_url = reverse_lazy('index')

class TodoJsonView(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request, *args, **kwargs):
        todos = Todo.objects.filter(done=True).values()
        return JsonResponse({'todos': list(todos)})

def signupView(request):
  if request.method == 'POST':
    form = SignupForm(request.POST)
    pprint(vars(form))
    if form.is_valid():
      print("Form was valid")
      form.save()
      username = form.cleaned_data.get('username')
      signup_user = User.objects.get(username=username)
      customer_group = Group.objects.get(name='Customer')
      customer_group.user_set.add(signup_user)
    else:
      print('Something went wrong')
  else:  
    form = SignupForm()
  return render(request, 'accounts/signup.html', {'form':form})  

def signinView(request):
  print(request.method)  
  if request.method == 'POST':
    form = AuthenticationForm(data=request.POST)
    pprint(vars(form))
    if form.is_valid():
      print("Form was valid")
      username = request.POST['username']
      password = request.POST['password']
      print("username={}, password={}".format(username, password))
      user = authenticate(username=username, password=password)
      pprint(vars(user))
      if user is not None:
        login(request, user)
        return redirect('index')
      else:
        return redirect('signup')
    else:
        print('Invalid form?')
  else:
    print('get request?')  
    form = AuthenticationForm()
  return render(request, 'accounts/signin.html', {'form':form})  

def signoutView(request):
  logout(request)
  return redirect('signin')
