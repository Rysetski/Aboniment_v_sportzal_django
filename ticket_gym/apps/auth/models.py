from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Кастомная модель пользователя"""
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(
        upload_to='profile_pics/', blank=True, null=True)
