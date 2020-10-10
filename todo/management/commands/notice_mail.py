<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> f466b8e... スペルミスの修正
import datetime
import pytz
from django.utils import timezone
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from todo.models import Task
<<<<<<< HEAD
=======
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
>>>>>>> 51b8f18... プッシュとメール通知の準備
=======
>>>>>>> f466b8e... スペルミスの修正

from typing import List

tzname: str = 'Asia/Tokyo'


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
        nearby_tasks: List[Task] = Task.objects.filter(deadline__lt=timezone.now()+datetime.timedelta(days=1))
        for user in User.objects.all():
            tasks: Task = nearby_tasks.filter(group__in=user.groups.all()).order_by('deadline')
            if tasks and user.email:
                message: str = ""
                for task in tasks:
                    deadline_str: str = task.deadline.astimezone(pytz.timezone(tzname)).strftime('%m/%d %H:%M')
                    message += "{0} {1} 〆切\n".format(task.task_text, deadline_str)
                user.email_user(subject, message, from_email)
        """
