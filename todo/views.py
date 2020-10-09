import datetime
import pytz
from django.utils import timezone
from django.shortcuts import render, redirect

from .models import Task

# Create your views here.

tzname = 'Asia/Tokyo'


def todolist(request) -> render:
    return render_todolist(request, "")


def add(request) -> render:
    try:
        task_text = request.POST['task_text']
    except (KeyError):
        return render_todolist(request, "Trouble with task_text")
    try:
        deadline_str = request.POST['deadline']
    except (KeyError):
        return render_todolist(request, "Trouble with deadline")
    deadline = str_to_dt(deadline_str)
    Task.objects.create(task_text=task_text, deadline=deadline)
    return redirect('todo:todolist')


def delete_modify(request) -> render:
    try:
        operation: str = request.POST['operation']
    except(KeyError, Task.DoesNotExist):
        return render_todolist(request, "Trouble with operation")
    try:
        task: Task = Task.objects.get(pk=request.POST['task_id'])
    except(KeyError, Task.DoesNotExist):
        return render_todolist(request, "Trouble with task_id")

    if operation == 'delete':
        task.delete()

    elif operation == 'modify':
        try:
            task_text: str = request.POST['task_text']
        except (KeyError):
            return render_todolist(request, "Trouble with task_text")
        try:
            deadline_str: str = request.POST['deadline']
        except (KeyError):
            return render_todolist(request, "Trouble with deadline")
        deadline = str_to_dt(deadline_str)
        task.task_text = task_text
        task.deadline = deadline
        task.save()

    return redirect('todo:todolist')


def render_todolist(request, error_message: str) -> render:
    return render(request, 'todolist.html', {
        'tzname': tzname,
        'current_time': timezone.now(),
        'task_list': Task.objects.order_by('deadline'),
        'error_message': error_message,
    })


def str_to_dt(dt_str: str):
    dt_naive = datetime.datetime.strptime(dt_str, "%Y-%m-%dT%H:%M")
    dt_aware = timezone.make_aware(dt_naive, pytz.timezone(tzname))
    return dt_aware
