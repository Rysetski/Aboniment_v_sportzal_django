from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser, Gym, Subscription, Discount, Notification
from .serializers import UserSerializer, GymSerializer, SubscriptionSerializer, DiscountSerializer, NotificationSerializer


class SubscriptionListView(APIView):
    """Список всех абонементов"""

    def get(self, request):
        subscriptions = Subscription.objects.filter(user=request.user)
        serializer = SubscriptionSerializer(subscriptions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SubscriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubscriptionDetailView(APIView):
    """Детали абонемента"""

    def get(self, request, pk):
        subscription = get_object_or_404(
            Subscription, pk=pk, user=request.user)
        serializer = SubscriptionSerializer(subscription)
        return Response(serializer.data)
