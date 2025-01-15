from django.db import models
from apps.auth.models import CustomUser  # Для связи с пользователем
from apps.gyms.models import Gym         # Для связи с моделью Gym


class Subscription(models.Model):
    """Модель абонемента"""
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Абонемент {self.user.username} в {self.gym.name}"
