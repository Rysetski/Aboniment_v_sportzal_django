from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser, Gym, Subscription, Discount, Notification
from .serializers import UserSerializer, GymSerializer, SubscriptionSerializer, DiscountSerializer, NotificationSerializer

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Кастомная модель пользователя"""
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(
        upload_to='profile_pics/', blank=True, null=True)
