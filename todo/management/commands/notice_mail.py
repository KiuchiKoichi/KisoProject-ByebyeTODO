import datetime
import pytz
from django.utils import timezone
from django.core.management.base import BaseCommand
from todo.models import Task
from django.contrib.auth import get_user_model
User = get_user_model()

from typing import List


class Command(BaseCommand):
    def handle(self, *args, **options) -> None:
        subject: str = "もうすぐ〆切！"
        from_email: str = "ByeByeTODO <kisopro.byebyetodo@gmail.com>"
        nearby_tasks: List[Task] = Task.objects.filter(deadline__gt=timezone.now(), deadline__lt=timezone.now()+datetime.timedelta(days=1))
        for user in User.objects.all():
            tasks: Task = nearby_tasks.filter(group__in=user.groups.all()).order_by('deadline')
            if tasks and user.accept_email:
                message: str = ""
                for task in tasks:
                    deadline_str: str = task.deadline.astimezone(pytz.timezone(user.tz)).strftime('%m/%d %H:%M')
                    message += "{}\t{}\t{} 〆切\n".format(task.group.name[:-10], task.task_text, deadline_str)
                user.email_user(subject, message, from_email)
