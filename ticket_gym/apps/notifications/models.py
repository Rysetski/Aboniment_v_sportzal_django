from django.db import models
from apps.auth.models import CustomUser  # Для связи с пользователем


class Notification(models.Model):
    """Модель уведомлений"""
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Уведомление для {self.user.username}"
