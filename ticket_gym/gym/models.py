from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from django.core.mail import send_mail

# Кастомная модель пользователя для добавления дополнительных полей


class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)

# Модель спортзала для описания его характеристик


class Gym(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    address = models.TextField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

# Модель комментариев для отзывов о спортзалах


class GymComment(models.Model):
    gym = models.ForeignKey(
        Gym, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Комментарий от {self.user.username} к {self.gym.name}"

# Модель подписки для членств


class Subscription(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="subscriptions")
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE,
                            related_name="subscriptions")
    start_date = models.DateField(default=now)
    end_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.user.username} - {self.gym.name}"

    def is_active(self):
        return self.end_date >= now().date()

# Модель уведомлений о завершении подписки


class Notification(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="notifications")
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

# Модель промокодов


class Promocode(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount_percentage = models.PositiveIntegerField()  # Скидка в процентах
    valid_from = models.DateTimeField()
    valid_until = models.DateTimeField()

    def is_valid(self):
        return self.valid_from <= now() <= self.valid_until

# Модель тренера


class Trainer(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()
    training_types = models.TextField()  # Список типов тренировок через запятую
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2)
    gym = models.ForeignKey(
        Gym, on_delete=models.CASCADE, related_name="trainers")

    def __str__(self):
        return self.name

# Модель записи на тренировку


class TrainingSession(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="training_sessions")
    trainer = models.ForeignKey(
        Trainer, on_delete=models.CASCADE, related_name="sessions")
    session_date = models.DateTimeField()
    duration_in_hours = models.DecimalField(max_digits=3, decimal_places=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.total_price = self.duration_in_hours * self.trainer.price_per_hour
        super().save(*args, **kwargs)
