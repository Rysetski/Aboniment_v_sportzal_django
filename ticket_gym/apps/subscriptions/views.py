from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Subscription
from .serializers import SubscriptionSerializer
from notifications.tasks import send_notification  # Импорт задачи


class SubscriptionListView(APIView):
    """Список всех абонементов"""

    def post(self, request):
        serializer = SubscriptionSerializer(data=request.data)
        if serializer.is_valid():
            subscription = serializer.save(user=request.user)
            # Запуск задачи Celery для отправки уведомления
            send_notification.delay(
                user_id=request.user.id,
                message=f"Вы оформили подписку на {subscription.gym.name}"
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubscriptionDetailView(APIView):
    """Детали абонемента"""

    def get(self, request, pk):
        subscription = get_object_or_404(
            Subscription, pk=pk, user=request.user)
        serializer = SubscriptionSerializer(subscription)
        return Response(serializer.data)

    def put(self, request, pk):
        subscription = get_object_or_404(
            Subscription, pk=pk, user=request.user)
        serializer = SubscriptionSerializer(subscription, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        subscription = get_object_or_404(
            Subscription, pk=pk, user=request.user)
        subscription.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
