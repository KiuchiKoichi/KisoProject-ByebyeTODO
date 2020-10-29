import datetime
import pytz
from django.utils import timezone
from django.core.management.base import BaseCommand
from django.urls import reverse
from django.contrib.auth.models import Group
from todo.models import Task
from webpush import send_user_notification, send_group_notification
from django.contrib.auth import get_user_model
User = get_user_model()

from typing import Dict, List

""" htmlの記述
{% load webpush_notifications %}
<head>
  {% webpush_header %}
</head>
<body>
  {% webpush_button %}
</body>
"""


class Command(BaseCommand):
    def handle(self, *args, **options) -> None:
        payload: Dict[str, str] = {
            "head": "もうすぐ〆切！",
        }
        nearby_tasks: List[Task] = Task.objects.filter(deadline__gt=timezone.now(), deadline__lt=timezone.now()+datetime.timedelta(days=1))
        for user in User.objects.all():
            tasks: Task = nearby_tasks.filter(group__in=user.groups.all()).order_by('deadline')
            if tasks:
                task = tasks[0]
                payload["icon"] = "/static/images/icon_" + user.mycolor + ".png"
                payload["url"] = reverse('todo:todolist', args=[task.group.id])
                deadline_str: str = task.deadline.astimezone(pytz.timezone(user.tz)).strftime('%m/%d %H:%M')
                payload["body"] = "{}\t{} 〆切".format(task.task_text, deadline_str)
                send_user_notification(user=user, payload=payload, ttl=1000)
