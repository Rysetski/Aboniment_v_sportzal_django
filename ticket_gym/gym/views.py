from rest_framework import viewsets
from .models import Gym, GymComment, Subscription, Notification, Promocode, Trainer, TrainingSession
from .serializers import (
    GymSerializer,
    GymCommentSerializer,
    SubscriptionSerializer,
    NotificationSerializer,
    PromocodeSerializer,
    TrainerSerializer,
    TrainingSessionSerializer,
)


class GymViewSet(viewsets.ModelViewSet):
    queryset = Gym.objects.all()
    serializer_class = GymSerializer


class GymCommentViewSet(viewsets.ModelViewSet):
    queryset = GymComment.objects.all()
    serializer_class = GymCommentSerializer


class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


class PromocodeViewSet(viewsets.ModelViewSet):
    queryset = Promocode.objects.all()
    serializer_class = PromocodeSerializer


class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer


class TrainingSessionViewSet(viewsets.ModelViewSet):
    queryset = TrainingSession.objects.all()
    serializer_class = TrainingSessionSerializer
