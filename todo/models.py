from django.db import models
from django.contrib.auth.models import Group
# Create your models here.


class Task(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    task_text = models.CharField(max_length=200)
    deadline = models.DateTimeField()

    def __str__(self) -> str:
        return self.task_text
