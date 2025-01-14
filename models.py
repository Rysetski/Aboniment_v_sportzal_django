from django.db import models
from django.contrib.auth.models import User


class Gym(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} - {self.gym.name}"


class Trainer(models.Model):
    name = models.CharField(max_length=255)
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE)
    expertise = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class TrainingSession(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    date = models.DateTimeField()
    duration = models.IntegerField()  # duration in minutes
    max_participants = models.IntegerField()

    def __str__(self):
        return f"{self.trainer.name} - {self.date}"
