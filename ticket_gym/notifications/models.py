from django.db import models
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser, Gym, Subscription, Discount, Notification
from .serializers import UserSerializer, GymSerializer, SubscriptionSerializer, DiscountSerializer, NotificationSerializer
# Create your models here.


class Notification(models.Model):
    """Модель уведомлений"""
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Уведомление для {self.user.username}"
