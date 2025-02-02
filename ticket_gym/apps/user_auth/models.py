from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Кастомная модель пользователя"""
    email = models.EmailField(unique=True, blank=False, null=False)
    profile_picture = models.ImageField(
        upload_to='profile_pics/', blank=True, null=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Уникальное имя обратной связи
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions_set',  # Уникальное имя обратной связи
        blank=True,
    )
