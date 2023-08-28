from django.contrib.auth import get_user_model
from django.forms import ModelChoiceField
from django.test import TestCase
from django.urls import reverse

from home.forms import WorkerCreationForm
from home.models import Position, Worker, TaskType


class FormTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_superuser(
            username="test",
            password="pass12345678",
            first_name="Test first",
            last_name="Test last",
        )
        self.position = Position.objects.create(position="QA")

        self.client.force_login(self.user)

    def test_create_worker_is_valid(self):
        form_data = {
            "username": "mac_username",
            "first_name": "Mac First",
            "last_name": "Mac Last",
            # "position": 1,
            "password1": "Qwerty1234567",
            "password2": "Qwerty1234567",
        }

        # Worker.objects.create(
        #     username="mac_username",
        #     first_name="First",
        #     last_name="Last",
        #     position=self.position,
        #     password="Qwerty1234567",
        # )
        form = WorkerCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

        response = self.client.post(reverse('home:worker-create'), data=form_data)
        new_worker = get_user_model().objects.all()
        # #
        a = 5

    def test_search_form_is_work_in_position_list(self):
        text_to_filter = "QA"
        data = {
            "position": text_to_filter
        }

        Position.objects.create(position="Sale")
        Position.objects.create(position="Dev")
        Position.objects.create(position="Designer")

        response = self.client.get(reverse("home:position-list"), data=data)

        positions_after_filter_on_page = response.context_data["position_list"]
        positions_to_filter = Position.objects.filter(position=data["position"])

        self.assertEqual(
            list(positions_after_filter_on_page),
            list(positions_to_filter)
        )

    def test_search_form_is_work_in_task_type_list(self):
        text_to_filter = "Dev"
        data = {
            "name": text_to_filter
        }

        TaskType.objects.create(name="Design")
        TaskType.objects.create(name="Content create")
        TaskType.objects.create(name="Dev")

        response = self.client.get(reverse("home:task-type-list"), data=data)

        positions_after_filter_on_page = response.context_data["task_type_list"]
        positions_to_filter = TaskType.objects.filter(name=data["name"])

        self.assertEqual(
            list(positions_after_filter_on_page),
            list(positions_to_filter)
        )

    def test_search_form_is_work_in_task_type_list(self):
        text_to_filter = "Dev"
        data = {
            "name": text_to_filter
        }

        TaskType.objects.create(name="Design")
        TaskType.objects.create(name="Content create")
        TaskType.objects.create(name="Dev")

        response = self.client.get(reverse("home:task-type-list"), data=data)

        positions_after_filter_on_page = response.context_data["task_type_list"]
        positions_to_filter = TaskType.objects.filter(name=data["name"])

        self.assertEqual(
            list(positions_after_filter_on_page),
            list(positions_to_filter)
        )

    def test_search_form_is_work_in_worker_list(self):
        text_to_filter = "User1"
        data = {
            "name": text_to_filter
        }

        Worker.objects.create(
            username="user1",
            password="pass12345678",
            first_name="User1",
            last_name="Last",
        )
        Worker.objects.create(
            username="user2",
            password="pass12345678",
            first_name="User2",
            last_name="Last",
        )

        response = self.client.get(reverse("home:worker-list"), data=data)

        positions_after_filter_on_page = response.context_data["worker_list"]
        positions_to_filter = Worker.objects.filter(first_name=data["name"])

        self.assertEqual(
            list(positions_after_filter_on_page),
            list(positions_to_filter)
        )

    def test_search_form_is_work_in_worker_list(self):
        text_to_filter = "User1"
        data = {
            "name": text_to_filter
        }

        Worker.objects.create(
            username="user1",
            password="pass12345678",
            first_name="User1",
            last_name="Last",
        )
        Worker.objects.create(
            username="user2",
            password="pass12345678",
            first_name="User2",
            last_name="Last",
        )

        response = self.client.get(reverse("home:worker-list"), data=data)

        positions_after_filter_on_page = response.context_data["worker_list"]
        positions_to_filter = Worker.objects.filter(first_name=data["name"])

        self.assertEqual(
            list(positions_after_filter_on_page),
            list(positions_to_filter)
        )
