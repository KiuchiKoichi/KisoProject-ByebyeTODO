import datetime
import pytz
from django.utils import timezone
from django.core.management.base import BaseCommand
from django.urls import reverse
from django.contrib.auth.models import User, Group
from todo.models import Task
from webpush import send_user_notification, send_group_notification
"""
from account.models import UserSetting
"""

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
        # 基本形
        user: User = User.objects.get(username="testuser")
        url: str = reverse('todo:todolist')
        payload: Dict[str, str] = {
            "head": "ByeByeTODO",
            "body": "量子力学の課題 10/12 23:59 〆切",
            "icon": "/static/images/icon_pushnotice.jpg",
            "url": url,
        }
        send_user_notification(user=user, payload=payload, ttl=10)

        """Taskにgroup:ForeignKeyを設定してから
        payload: Dict[str, str] = {
            "head": "もうすぐ〆切！",
            "icon": "/static/images/icon_pushnotice.jpg",
        }
        nearby_tasks: List[Task] = Task.objects.filter(deadline__gt=timezone.now(), deadline__lt=timezone.now()+datetime.timedelta(days=1))
        for group in Group.objects.all():
            task: Task = nearby_tasks.filter(group=group).order_by('deadline')[0]
            if task:
                setting, created = UserSetting.objects.get_or_create(user=user)
                deadline_str: str = task.deadline.astimezone(pytz.timezone(setting.tz)).strftime('%m/%d %H:%M')
                payload["body"] = "{0} {1} 〆切".format(task.task_text, deadline_str)
                payload["url"] = reverse('todo:todolist', group.pk),
                send_group_notification(group_name=group.name, payload=payload, ttl=1000)
        """
