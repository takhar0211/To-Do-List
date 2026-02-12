from gc import get_objects
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import tasks


# Create your views here.
def home(request):
    task = tasks.objects.filter(is_completed = False).order_by('-updated_at')
    completed_task = tasks.objects.filter(is_completed = True).order_by('-updated_at')
    context = {
        'tasks': task,
        'completed_task':completed_task,
    }
    return render(request,'index.html',context)

def addTask(request):
    task = request.POST['task']
    tasks.objects.create(task_name = task)
    return redirect('home')

def markAsDone(request,pk):
    task = get_object_or_404(tasks,pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def markAsUnDone(request,pk):
    task = get_object_or_404(tasks,pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def deleteTask(request,pk):
    task = get_object_or_404(tasks,pk=pk)
    task.delete()
    return redirect('home')

def editTask(request,pk):
    task = get_object_or_404(tasks,pk=pk)
    if(request.method == 'POST'):
        new_task = request.POST['new_task']
        task.task_name = new_task
        task.save()
        return redirect('home')
    else:
        return render(request,'editTask.html',{'task':task})

