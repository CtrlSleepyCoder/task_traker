from django.shortcuts import render, redirect
from .models import Task



def index(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)

    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})



def toggle_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.done = not task.done
    task.save()
    return redirect('/')



def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('/')



def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)

    if request.method == 'POST':
        new_title = request.POST.get('title')
        if new_title:
            task.title = new_title
            task.save()
            return redirect('/')

    return render(request, 'edit.html', {'task': task})



def completed_tasks(request):
    tasks = Task.objects.filter(done=True)
    return render(request, 'index.html', {'tasks': tasks})


def pending_tasks(request):
    tasks = Task.objects.filter(done=False)
    return render(request, 'index.html', {'tasks': tasks})