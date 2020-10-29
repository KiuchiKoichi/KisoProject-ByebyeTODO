import datetime
import pytz
import time
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from .models import Task
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.


@login_required
def create_group(request) -> render:
    try:
        name: str = request.POST['name']
    except (KeyError):
        messages.error(request, "グループ名を取得できません")
        return redirect('accounts:profile')
    name += str(time.time())[-10:]
    group = Group.objects.create(name=name)
    group.user_set.add(request.user)
    return redirect('todo:todolist', group.pk)


@login_required
def update_group(request) -> render:
    try:
        name: str = request.POST['name']
    except (KeyError):
        messages.error(request, "グループ名を取得できません")
        return redirect('accounts:profile')
    try:
        group = Group.objects.get(pk=request.POST['pk'])
    except(KeyError, Group.DoesNotExist):
        messages.error(request, "idまたはグループを取得できません")
        return redirect('accounts:profile')
    if request.user not in group.user_set.all():
        messages.error(request, "あなたのグループではありません")
        return redirect('accounts:profile')
    name += str(time.time())[-10:]
    group.name = name
    group.save()
    return redirect('accounts:profile')


@login_required
def delete_group(request) -> render:
    try:
        group = Group.objects.get(pk=request.POST['pk'])
    except(KeyError, Group.DoesNotExist):
        messages.error(request, "idまたはグループを取得できません")
    group.user_set.remove(request.user)
    if not group.user_set.all().exists():
        group.delete()
    return redirect('accounts:profile')


@login_required
def todolist(request, group_id: int) -> render:
    try:
        group = Group.objects.get(pk=group_id)
    except (KeyError, Group.DoesNotExist):
        messages.error(request, "グループを取得できませんでした")
        return redirect('accounts:profile')
    if request.user not in group.user_set.all():
        messages.error(request, "あなたのグループではありません")
        return redirect('accounts:profile')
    overdue_list, nearby_list, other_list = [], [], []
    now: datetime.datetime = timezone.now()
    tommorow: datetime.datetime = now + datetime.timedelta(days=1)
    for task in group.task_set.order_by('deadline'):
        deadline: datetime.datetime = task.deadline
        if deadline < now:
            overdue_list.append(task)
        elif deadline < tommorow:
            nearby_list.append(task)
        else:
            other_list.append(task)
    return render(request, 'todolist.html', {
        'group': group,
        'overdue_list': overdue_list,
        'nearby_list': nearby_list,
        'other_list': other_list,
    })


@login_required
def create_task(request, group_id: int) -> render:
    try:
        group = Group.objects.get(pk=group_id)
    except (KeyError, Group.DoesNotExist):
        messages.error(request, "グループを取得できませんでした")
        return redirect('accounts:profile')
    if request.user not in group.user_set.all():
        messages.error(request, "あなたのグループではありません")
        return redirect('accounts:profile')
    try:
        task_text: str = request.POST['task_text']
    except (KeyError):
        messages.error(request, "タスク名を取得できません")
        return redirect('todo:todolist', group_id)
    try:
        deadline_str: str = request.POST['deadline']
    except (KeyError):
        messages.error(request, "〆切を取得できません")
        return redirect('todo:todolist', group_id)
    deadline: datetime.datetime = str_to_dt(deadline_str, request.user.tz)
    group.task_set.create(task_text=task_text, deadline=deadline)
    return redirect('todo:todolist', group_id)


@login_required
def update_task(request, group_id: int) -> render:
    try:
        group = Group.objects.get(pk=group_id)
    except (KeyError, Group.DoesNotExist):
        messages.error(request, "グループを取得できませんでした")
        return redirect('accounts:profile')
    if request.user not in group.user_set.all():
        messages.error(request, "あなたのグループではありません")
        return redirect('accounts:profile')
    try:
        task_text: str = request.POST['task_text']
    except (KeyError):
        messages.error(request, "タスク名を取得できません")
        return redirect('todo:todolist', group_id)
    try:
        deadline_str: str = request.POST['deadline']
    except (KeyError):
        messages.error(request, "〆切を取得できません")
        return redirect('todo:todolist', group_id)
    try:
        task = Task.objects.get(pk=request.POST['task_id'])
    except(KeyError, Task.DoesNotExist):
        messages.error(request, "idまたはタスクを取得できません")
        return redirect('todo:todolist', group_id)
    deadline: datetime.datetime = str_to_dt(deadline_str, request.user.tz)
    task.task_text = task_text
    task.deadline = deadline
    task.save()
    return redirect('todo:todolist', group_id)


@login_required
def delete_task(request, group_id: int) -> render:
    try:
        group = Group.objects.get(pk=group_id)
    except (KeyError, Group.DoesNotExist):
        messages.error(request, "グループを取得できませんでした")
        return redirect('accounts:profile')
    if request.user not in group.user_set.all():
        messages.error(request, "あなたのグループではありません")
        return redirect('accounts:profile')
    try:
        task = Task.objects.get(pk=request.POST['task_id'])
    except(KeyError, Task.DoesNotExist):
        messages.error(request, "idまたはタスクを取得できません")
        return redirect('todo:todolist', group_id)
    task.delete()
    return redirect('todo:todolist', group_id)


def str_to_dt(dt_str: str, tz: str) -> datetime.datetime:
    dt_naive: datetime.datetime = datetime.datetime.strptime(dt_str, "%Y-%m-%dT%H:%M")
    dt_aware: datetime.datetime = timezone.make_aware(dt_naive, pytz.timezone(tz))
    return dt_aware
