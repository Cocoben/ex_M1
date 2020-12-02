from django.shortcuts import render
from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.utils import timezone

from django.urls import reverse

from .models import Task

def index(request):
    tasks_list = Task.objects.all()
    context = {
        'tasks_list': tasks_list,
    }
    #output = ",".join([q.content for q in tasks_list])

    #template = loader.get_template('todo/index.html')
    #return HttpResponse(template.render(context, request))

    #Raccourcis
    return render(request, 'todo/index.html', context)

def edit(request, task_id):
    # response = "Vous pouvez modifier la tâche %s."
    # return HttpResponse(response % task_id)
    if request.POST :
        task = get_object_or_404(Task, pk=task_id)
        task.content = request.POST['content']
        task.save()
        return HttpResponseRedirect(reverse('todo:index'))
    else :
        task = Task.objects.get(pk=task_id)
        return render(request, 'todo/edit.html', {'task': task})


def new(request):
    task = Task(content=request.POST['new_task'],created_date=timezone.now())
    task.save()
    return HttpResponseRedirect(reverse('todo:index'))

def delete(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return HttpResponseRedirect(reverse('todo:index'))

def done(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.is_done = 1
    task.save()
    return HttpResponseRedirect(reverse('todo:index'))
    