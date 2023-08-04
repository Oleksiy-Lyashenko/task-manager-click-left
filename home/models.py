from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Position(models.Model):
    position = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["position"]

    def __str__(self):
        return self.position


class TaskType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(
        Position,
        on_delete=models.SET_NULL,
        null=True,
        related_name="workers"
    )

    class Meta:
        ordering = ["username"]

    def __str__(self):
        return f"{self.username} - {self.first_name} {self.last_name}: {self.position}"


class Task(models.Model):
    PRIORITY_CHOICE = [
        ("Urgent", "Urgent priority"),
        ("High", "High priority"),
        ("Normal", "Normal priority"),
        ("Low", "Low priority"),
    ]

    name = models.CharField(max_length=255, null=False)
    description = models.TextField(null=False)
    deadline = models.DateTimeField(auto_now=False, null=False)
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(
        max_length=6,
        choices=PRIORITY_CHOICE,
        default="Normal"
    )
    task_type = models.ForeignKey(
        TaskType,
        on_delete=models.CASCADE,
        related_name="tasks"
    )
    assignees = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="tasks"
    )

    class Meta:
        ordering = ["-deadline"]

    def __str__(self):
        return f"{self.name} {self.task_type}"
