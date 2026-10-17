from django.shortcuts import redirect, render
from .models import Task
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import hashers

# Create your views here.
def login_user(request):
    data=request.POST
    if request.method=='POST':
        username=data.get('username')
        password=data.get('password')
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            messages.success(request,'Logged in successfully')
            return redirect('home_viewtask')
        else:
            messages.error(request,'Invalid username or password')
            return render(request,'login.html')
    return render(request,'login.html')

def register_user(request):
    data=request.POST
    if request.method=='POST':
        username=data.get('username')
        password=data.get('password')
        if User.objects.filter(username=username).exists():
            messages.error(request,'Username already exists')
            return render(request,'register.html')
        else:
            User.objects.create_user(username=username,password=password)
            messages.success(request,'User registered successfully')
            return render(request,'login.html')
    return render(request,'register.html')

def logout_user(request):
    logout(request)
    messages.success(request,'Logged out successfully')
    return render(request,'login.html')

@login_required
def home_addtask(request):
    data=request.POST
    if request.method=='POST':
        user=request.user
        title=data.get('title')
        work=data.get('work')
        status=data.get('status')
        Task.objects.create(user1=user,title=title,work=work,status=status)
        return redirect('home_viewtask')
    return render(request,'home.html')

@login_required
def home_viewtask(request):
    task = Task.objects.filter(user1=request.user)
    return render(request, 'home.html', {'task': task})

@login_required
def home_deletetask(request,task_id):
    user=request.user
    task=Task.objects.get(id=task_id,user1=user)
    task.delete()
    messages.success(request,'Task deleted successfully')
    return redirect('home_viewtask')

@login_required
def edit_task(request,task_id):
    user=request.user
    task=Task.objects.get(id=task_id,user1=user)
    if request.method=='POST':
        data=request.POST
        task.title=data.get('title')
        task.work=data.get('work')
        task.status=data.get('status')
        task.save()
        messages.success(request,'Task updated successfully')
        return redirect('home_viewtask')
    return render(request,'edit_task.html',{'task':task})