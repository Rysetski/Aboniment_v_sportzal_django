from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Notification
from rest_framework.test import APIClient


class NotificationTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser', password='password')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.notification = Notification.objects.create(
            user=self.user,
            message="Test notification",
            is_read=False,
        )

    def test_get_notifications(self):
        response = self.client.get('/notifications/')
        self.assertEqual(response.status_code, 200)

    def test_mark_notification_as_read(self):
        response = self.client.post(
            f'/notifications/{self.notification.id}/mark-as-read/')
        self.assertEqual(response.status_code, 200)
        self.notification.refresh_from_db()
        self.assertTrue(self.notification.is_read)
