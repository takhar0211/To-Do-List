from gc import get_objects
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import tasks


# Create your views here.
def home(request):
    task = tasks.objects.filter(is_completed = False)
    context = {
        'tasks': task
    }
    return render(request,'index.html',context)

def addTask(request):
    task = request.POST['task']
    tasks.objects.create(task_name = task)
    return redirect('home')