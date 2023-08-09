from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from home.forms import WorkerCreationForm
from home.models import Position


class FormTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="pass12345678",
            first_name="Test first",
            last_name="Test last"
        )

        self.client.force_login(self.user)

    def test_create_worker_is_valid(self):
        position = Position.objects.create(position="QA")
        position.save()

        form_data = {
            "username": "mac",
            "password1": "MacBook21",
            "password2": "MacBook21",
            "first_name": "test first",
            "last_name": "test last",
            "position": position,
        }

        self.client.post(reverse('home:worker-create'), data=form_data)
        new_worker = get_user_model().objects.get(
            username=form_data["username"]
        )

        return len(list(new_worker)) == 2

