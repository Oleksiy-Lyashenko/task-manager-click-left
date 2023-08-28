from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from home.models import Position, TaskType, Task

TASK_URL = reverse("home:task-list")
WORKER_URL = reverse("home:worker-list")
POSITION_URL = reverse("home:position-list")
TASK_TYPE_URL = reverse("home:task-type-list")


class PublicViewTest(TestCase):
    def test_login_required_task_list(self):
        response1 = self.client.get(TASK_URL)
        response2 = self.client.get(WORKER_URL)
        response3 = self.client.get(POSITION_URL)
        response4 = self.client.get(TASK_TYPE_URL)

        self.assertNotEqual(response1.status_code, 200)
        self.assertNotEqual(response2.status_code, 200)
        self.assertNotEqual(response3.status_code, 200)
        self.assertNotEqual(response4.status_code, 200)


class PrivateViewTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="pass12345678",
            first_name="Test first",
            last_name="Test last",
        )

        self.client.force_login(self.user)

    def test_retrieve_position(self):
        Position.objects.create(position="QA")
        Position.objects.create(position="Developer")

        response = self.client.get(POSITION_URL)
        positions = Position.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["position_list"]),
            list(positions)
        )
        self.assertTemplateUsed("home/position_list.html")

    def test_retrieve_task_type(self):
        TaskType.objects.create(name="Create Page")
        TaskType.objects.create(name="Delete Page")

        response = self.client.get(TASK_TYPE_URL)
        task_types = TaskType.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["task_type_list"]),
            list(task_types)
        )
        self.assertTemplateUsed("home/task_type_list.html")

    def test_retrieve_worker(self):
        position = Position.objects.create(position="QA")

        get_user_model().objects.create_user(
            username="test1",
            password="pass12345678",
            first_name="Test first 1",
            last_name="Test last 1",
            position=position
        )
        get_user_model().objects.create_user(
            username="test2",
            password="pass12345678",
            first_name="Test first 2",
            last_name="Test last 2",
        )

        response = self.client.get(WORKER_URL)
        task_types = get_user_model().objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["worker_list"]),
            list(task_types)
        )
        self.assertTemplateUsed("home/worker_list.html")

    def test_retrieve_task(self):
        task_type = TaskType.objects.create(name="Features")
        Task.objects.create(
            name="Create Page",
            description="Create home page to site",
            deadline=datetime(2024, 8, 25),
            priority="Normal",
            task_type=task_type

        )
        Task.objects.create(
            name="Create Page 2",
            description="Create home page to site 2",
            deadline=datetime(2025, 8, 25),
            priority="Low",
            task_type=task_type
        )

        response = self.client.get(TASK_URL)
        tasks = Task.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["task_list"]),
            list(tasks)
        )
        self.assertTemplateUsed("home/task_list.html")


