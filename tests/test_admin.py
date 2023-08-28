from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse, resolve

from home.models import Position


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = get_user_model().objects.create_superuser(
            username="test",
            password="pass12345678",
            first_name="Test first",
            last_name="Test last",
        )
        self.client.force_login(self.user)

        position = Position.objects.create(position="QA")

        self.worker = get_user_model().objects.create_user(
            username="worker",
            password="Qwerty1234",
            first_name="First",
            last_name="Worker",
            position=position
        )

    def test_worker_position_listed(self):
        url = reverse("admin:home_worker_changelist")
        response = self.client.get(url)

        self.assertTrue(response, self.worker.position)

    def test_worker_detail_position_listed(self):
        url = reverse("admin:home_worker_change", args=[self.worker.id])
        response = self.client.get(url)

        self.assertTrue(response, self.worker.position)

    def test_worker_detail_additional_fields_listed(self):
        url = reverse("admin:home_worker_add")
        response = self.client.get(url)

        self.assertContains(response, self.worker.first_name)
        self.assertContains(response, self.worker.last_name)
        self.assertContains(response, self.worker.position)
