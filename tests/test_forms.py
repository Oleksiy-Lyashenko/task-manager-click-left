from django.contrib.auth import get_user_model
from django.test import TestCase

from home.forms import WorkerCreationForm
from home.models import Position


class FormTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test1234",
        )

        self.client.force_login(self.user)

    def test_create_worker(self):
        position = Position.objects.create(position="QA")
        position.save()

        form_data = {
            "username": "bit",
            "first_name": "test first",
            "last_name": "test last",
            "position": position,
            "password1": "test1234",
            "password2": "test1234",
        }

        form = WorkerCreationForm(data=form_data)
        bool_ = form.is_valid()

        self.assertTrue(form.is_valid())
