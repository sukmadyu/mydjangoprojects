from django.shortcuts import render
from .models import Todo

def todo_views(request):
    todo = Todo.objects.all()
    return render(request, 'todo/home.html', {'todo':todo})
