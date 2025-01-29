from celery import shared_task
from .models import Notification


@shared_task
def send_notification(user_id, message):
    from django.contrib.auth import get_user_model
    User = get_user_model()
    user = User.objects.get(id=user_id)
    Notification.objects.create(user=user, message=message)
    return f"Notification sent to {user.username}"




@shared_task
def test_task():
    print("Celery is working!")
    return "Task executed successfully"
