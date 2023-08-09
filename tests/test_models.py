import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase

from home.forms import TaskForm, TaskUpdateForm, WorkerCreationForm
from home.models import Position, TaskType, Task


class ModelsTests(TestCase):
    def test_position_str(self):
        position = Position.objects.create(position="UI Design")

        self.assertEqual(str(position), position.position)

    def test_task_type_str(self):
        task_type = TaskType.objects.create(name="Features")

        self.assertEqual(str(task_type), task_type.name)

    def test_worker_str(self):
        worker = get_user_model().objects.create_user(
            username="test",
            password="pass12345678",
            first_name="Test first",
            last_name="Test last"
        )

        self.assertEqual(str(worker), (
            f"{worker.username} - {worker.first_name} {worker.last_name}: {worker.position}"
        ))

    def test_task_str(self):
        task_type = TaskType.objects.create(name="Features")

        task = Task.objects.create(
            name="Create page",
            description="Create an additional page to home site",
            deadline="2023-08-25",
            task_type=task_type
        )

        self.assertEqual(str(task), f"{task.name} {task.task_type}")

    def test_create_task_with_deadline(self):
        task_type = TaskType.objects.create(name="Features")

        name = "Create page"
        description = "Create an additional page to home site"
        deadline = datetime.datetime(2023, 8, 25, 16, 30)

        task = Task.objects.create(
            name=name,
            description=description,
            deadline=deadline,
            task_type=task_type
        )

        self.assertEqual(task.name, name)
        self.assertEqual(task.description, description)
        self.assertEqual(task.deadline, deadline)

    def test_deadline_in_task_is_not_valid(self):
        task_type = TaskType.objects.create(name="Features")

        name = "Create page"
        description = "Create an additional page to home site"
        deadline = datetime.datetime(2022, 8, 25, 16, 30)

        task = TaskForm(
            data={
                "name": name,
                "description": description,
                "deadline": deadline,
                "task_type": task_type
            }
        )

        self.assertFalse(task.is_valid())



