import datetime
import pytz
from django.utils import timezone
from django.shortcuts import render

from .models import Task

# Create your views here.

tzname = 'Asia/Tokyo'


def todolist(request) -> render:
    context = {
        'tzname': tzname,
        'current_time': timezone.now(),
        'task_list': Task.objects.order_by('deadline'),
    }
    if request.method == 'POST':
        operation: str = request.POST['operation']
        if operation == 'add':
            context['error_message'] = add(request)
        elif operation == 'delete':
            context['error_message'] = delete(request)
        elif operation == 'modify':
            context['error_message'] = modify(request)
    return render(request, 'todolist.html', context)


def add(request) -> str:
    try:
        task_text = request.POST['task_text']
    except (KeyError):
        return "Trouble with task_text"
    try:
        deadline_str = request.POST['deadline']
    except (KeyError):
        return "Trouble with deadline"
    deadline = str_to_dt(deadline_str)
    Task.objects.create(task_text=task_text, deadline=deadline)
    return ""


def delete(request) -> str:
    try:
        task = Task.objects.get(pk=request.POST['task_id'])
    except(KeyError, Task.DoesNotExist):
        return "Trouble with task_id"
    task.delete()
    return ""


def modify(request) -> str:
    try:
        task_text = request.POST['task_text']
    except (KeyError):
        return "Trouble with task_text"
    try:
        deadline_str = request.POST['deadline']
    except (KeyError):
        return "Trouble with deadline"
    try:
        task = Task.objects.get(pk=request.POST['task_id'])
    except(KeyError, Task.DoesNotExist):
        return "Trouble with task_id"
    deadline = str_to_dt(deadline_str)
    task.task_text = task_text
    task.deadline = deadline
    task.save()
    return ""


def str_to_dt(dt_str: str):
    dt_naive = datetime.datetime.strptime(dt_str, "%Y-%m-%dT%H:%M")
    dt_aware = timezone.make_aware(dt_naive, pytz.timezone(tzname))
    return dt_aware
