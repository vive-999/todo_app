from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.db.models import Sum

def home(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            try:
                finished = request.POST['is_finished']
                if finished == 'on':
                    finished = True
                else:
                    finished = False
            except:
                finished = False
            todos = Todo( title=request.POST['title'], is_finished=finished)
            todos.save()
            messages.success(
                request, 'Todo Added with !')
    else:
        form = TodoForm()
    todos = Todo.objects.all()
    print("here", todos)
    if len(todos) == 0:
        todos_done = True
    else:
        todos_done = False
    todos = zip(todos, range(1, len(todos)+1))
    context = {'form': form, 'todos': todos,
               'todos_done': todos_done}
    return render(request, 'prodapp/home.html', context)



def delete_todo(request, pk=None):
    Todo.objects.get(id=pk).delete()
    return redirect('home')


def update_todo(request, pk=None):
    todo = Todo.objects.get(id=pk)
    if todo.is_finished == True:
        todo.is_finished = False
    else:
        todo.is_finished = True
    todo.save()
    return redirect('home')

def reset_todo(request):
    todos = Todo.objects.all()
    for todo in todos:
        todo.is_finished = False
        todo.save()
    return redirect('home')

def completed_todo(request):
    todos = Todo.objects.filter(is_finished=True)
    print("here", todos)
    if len(todos) == 0:
        todos_done = True
    else:
        todos_done = False
    todos = zip(todos, range(1, len(todos)+1))
    context = { 'todos': todos,
               'todos_done': todos_done}
    return render(request, 'prodapp/completed.html', context)

def pending_todo(request):
    todos = Todo.objects.filter(is_finished=False)
    print("here", todos)
    if len(todos) == 0:
        todos_done = True
    else:
        todos_done = False
    todos = zip(todos, range(1, len(todos)+1))
    context = {'todos': todos,
               'todos_done': todos_done}
    return render(request, 'prodapp/pending.html', context)

