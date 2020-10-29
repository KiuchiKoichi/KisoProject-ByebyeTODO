import datetime
from django.db import models
from django.contrib.auth.models import Group
# Create your models here.


class Task(models.Model):
    group: Group = models.ForeignKey(Group, on_delete=models.CASCADE)
    task_text: str = models.CharField(max_length=200)
    deadline: datetime.datetime = models.DateTimeField()

    def __str__(self) -> str:
        return self.task_text
