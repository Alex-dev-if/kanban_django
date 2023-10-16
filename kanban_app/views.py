from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm 
import json


def home(request):
    task = Task.objects.all()
    tasks_todo = Task.objects.filter(status='To Do')
    tasks_doing = Task.objects.filter(status='Doing')
    tasks_done = Task.objects.filter(status='Done')
    
    return render(request, 'home.html', {
        'tasks_todo': tasks_todo,
        'tasks_doing': tasks_doing,
        'tasks_done': tasks_done,
        'task': task
    })
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            
            task = form.save()
            return redirect('task_detail', task_id=task.id)
    else:
        form = TaskForm()

    return render(request, 'create_task.html', {'form': form})

def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'task_detail.html', {'task': task})


def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    
    if request.method == 'GET':
        task.delete()
        return redirect('home')
    else:
        return redirect('home')
    
def task_edit(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm(instance=task)
    
    return render(request, 'task_edit.html', {'form': form, 'task': task})

def update_status(request, task_id, new_status):
    try:
        task = Task.objects.get(id=task_id)
        task.status = new_status
        task.save()
    except Task.DoesNotExist:
        pass  

    return redirect('home')  

def dashboard(request):
    todo_count = Task.objects.filter(status='To Do').count()
    doing_count = Task.objects.filter(status='Doing').count()
    done_count = Task.objects.filter(status='Done').count()
    data = {
        'todo_count': todo_count,
        'doing_count': doing_count,
        'done_count': done_count,
    }
    data_json = json.dumps(data)

    meses_done = Task.objects.filter(status='Done') \
                           .values_list('created_at__month', flat=True)
    return render(request, 'dashboard.html', {'meses_done': list(meses_done), 'data': data_json})