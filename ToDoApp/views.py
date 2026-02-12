from gc import get_objects
from django.shortcuts import get_object_or_404, render

from .models import tasks


# Create your views here.
def home(request):
    task = tasks.objects.all()
    context = {
        'task': task
    }
    return render(request,'index.html',context)