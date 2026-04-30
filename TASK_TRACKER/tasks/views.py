from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Task


@login_required
def index(request):
    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            Task.objects.create(title=title, user=request.user)

    tasks = Task.objects.filter(user=request.user)
    return render(request, "index.html", {"tasks": tasks})


def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        User.objects.create_user(username=username, password=password)
        return redirect("/login/")

    return render(request, "register.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("/")

    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("/login/")


def toggle(request, task_id):
    task = Task.objects.get(id=task_id)
    task.done = not task.done
    task.save()
    return redirect("/")


def delete(request, task_id):
    Task.objects.get(id=task_id).delete()
    return redirect("/")