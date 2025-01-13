from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser, Gym, Subscription, Discount, Notification
from .serializers import UserSerializer, GymSerializer, SubscriptionSerializer, DiscountSerializer, NotificationSerializer


class GymListView(APIView):
    """Список всех спортзалов"""

    def get(self, request):
        gyms = Gym.objects.all()
        serializer = GymSerializer(gyms, many=True)
        return Response(serializer.data)


class GymDetailView(APIView):
    """Детали конкретного спортзала"""

    def get(self, request, pk):
        gym = get_object_or_404(Gym, pk=pk)
        serializer = GymSerializer(gym)
        return Response(serializer.data)
