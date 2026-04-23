from django.shortcuts import render, redirect
from .models import Task

def index(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)

    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})


def toggle(request, task_id):
    task = Task.objects.get(id=task_id)
    task.done = not task.done
    task.save()
    return redirect('/')


def delete(request, task_id):
    Task.objects.get(id=task_id).delete()
    return redirect('/')