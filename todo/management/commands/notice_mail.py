import datetime, pytz
from django.utils import timezone
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from todo.models import Task
"""
from account.models import UserSetting
from django.core.mail import send_mail
"""

from typing import List


class Command(BaseCommand):
    def handle(self, *args, **options) -> None:
        # 基本
        user: User = User.objects.get(username="testuser")
        subject: str = "notice_mail"
        message: str = "Can you listen to me?"
        from_email: str = "ByeByeTODO <kisopro.byebyetodo@gmail.com>"
        user.email_user(subject, message, from_email)

        """Taskにgroup:ForeignKeyを設定してから
        subject: str = "もうすぐ〆切！"
        from_email: str = "ByeByeTODO <kisopro.byebyetodo@gmail.com>"
        nearby_tasks: List[Task] = Task.objects.filter(deadline__gt=timezone.now(), deadline__lt=timezone.now()+datetime.timedelta(days=1))
        for user in User.objects.all():
            tasks: List[Task] = nearby_tasks.filter(group__in=user.groups.all()).order_by('deadline')
            setting, created = UserSetting.objects.get_or_create(user=user)
            if tasks and setting.email and setting.accept_email:
                recipient_list = [setting.email]
                message: str = ""
                for task in tasks:
                    deadline_str: str = task.deadline.astimezone(pytz.timezone(setting.tz)).strftime('%m/%d %H:%M')
                    message += "{0}\t{1}\t〆切\n".format(task.task_text, deadline_str)
                send_mail(subject, message, from_email, recipient_list)
        """
