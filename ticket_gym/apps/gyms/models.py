from django.db import models
# Для связи с пользователем, если потребуется
from apps.user_auth.models import CustomUser


# Create your models here.
class Gym(models.Model):
    """Модель спортзала"""
    name = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    image = models.ImageField(upload_to='gym_images/', blank=True, null=True)
    first_prise = models.IntegerField(default=50)

    def __str__(self):
        return self.name
