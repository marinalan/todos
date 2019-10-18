from datetime import datetime
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse

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
