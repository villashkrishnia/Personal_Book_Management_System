from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .forms import TaskForm, TagForm
from .models import Task,Tag


@login_required(login_url='login')
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(data=request.POST)
        form.instance.user = request.user
        if form.is_valid():
            task = form.save()
            return redirect('dashboard')
    else:
        form = TaskForm()
    return render(request, 'tasks_and_tags/add_task.html', {'form': form})


@login_required(login_url='login')
def add_tag(request):
    if request.method == 'POST':
        form = TagForm(data=request.POST)
        form.instance.user = request.user
        if form.is_valid():
            tag = form.save()
            return redirect('dashboard')
    else:
        form = TagForm()
    return render(request, 'tasks_and_tags/add_tag.html', {'form': form})


@login_required(login_url='login')
def delete_task(request, pk):
     #task=Task.objects.all()
    task = Task.objects.get(id=pk)
    if request.method == "POST":
        task.delete()
        return redirect('dashboard')
    return render(request,'tasks_and_tags/delete_task.html',{'task':task})


@login_required(login_url='login')
def delete_tag(request, pk):
     #task=Tag.objects.all()
    tag =Tag.objects.get(id=pk)
    if request.method == "POST":
        tag.delete()
        return redirect('dashboard')
    return render(request,'tasks_and_tags/delete_tag.html',{'tag':tag})


@login_required(login_url='login')
def edit_task(request,pk):
    task=Task.objects.get(id=pk)
    if request.method=="POST":
        form = TaskForm(data=request.POST,instance=task)
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form=TaskForm(instance=task)
    return render(request, 'tasks_and_tags/add_task.html', {'form':form})

@login_required(login_url='login')
def mark_complete(request,pk):
    Task.objects.filter(id=pk).update(status="CO")
    Task.objects.filter(id=pk).update(completed_at=timezone.now())
    return redirect('dashboard')


@login_required(login_url='login')
def mark_pending(request,pk):
    Task.objects.filter(id=pk).update(status="PE")
    Task.objects.filter(id=pk).update(completed_at=None)
    return redirect('dashboard')
