import datetime
import pytz
from django.utils import timezone
from django.core.management.base import BaseCommand
from django.urls import reverse
from django.contrib.auth.models import User, Group
from todo.models import Task
from webpush import send_user_notification, send_group_notification

from typing import Dict, List

""" htmlの記述
<head>
  {% webpush_header %}
</head>
<body>
  {% webpush_button %}
</body>
"""

tzname: str = 'Asia/Tokyo'


class Command(BaseCommand):
    def handle(self, *args, **options) -> None:
        # 基本形
        user: User = User.objects.get(username="testuser")
        url: str = reverse('todo:todolist')
        payload: Dict[str, str] = {
            "head": "ByeByeTODO",
            "body": "量子力学の課題 10/12 23:59 〆切",
            "icon": "/static/images/webpush_icon_test.png",
            "url": url,
        }
        send_user_notification(user=user, payload=payload, ttl=10)

        """Taskにgroup:ForeignKeyを設定してから
        payload: Dict[str, str] = {
            "head": "もうすぐ〆切！",
            "icon": "/static/images/webpush_icon_test.png",
            "url": reverse('todo:todolist'),
        }
        nearby_tasks: List[Task] = Task.objects.filter(deadline__lt=timezone.now()+datetime.timedelta(days=1))
        for group in Group.objects.all():
            task: Task = nearby_tasks.filter(group__id=group.id).order_by('deadline')[0]
            if task:
                deadline_str: str = task.deadline.astimezone(pytz.timezone(tzname)).strftime('%m/%d %H:%M')
                payload["body"] = "{0} {1} 〆切".format(task.task_text, deadline_str)
                send_group_notification(group_name=group.name, payload=payload, ttl=1000)
        """
