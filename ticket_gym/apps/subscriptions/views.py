from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Subscription
from apps.gyms.models import Gym
from .serializers import SubscriptionSerializer
from apps.notifications.tasks import send_notification
from datetime import datetime, timedelta
from apps.discounts.models import Discount







@login_required
def subscription_list(request):
    """Отображение личного кабинета с абонементами"""
    subscriptions = Subscription.objects.filter(user=request.user)
    return render(request, 'subscriptions/subscription_list.html', {'subscriptions': subscriptions})


# @login_required
# def buy_subscription(request):
#     """Страница покупки абонемента"""
#     gyms = Gym.objects.all()  # Все тренажёрные залы
#     if request.method == 'POST':
#         gym_id = request.POST.get('gym')
#         start_date = datetime.strptime(
#             request.POST.get('start_date'), '%Y-%m-%d').date()
#         end_date = datetime.strptime(
#             request.POST.get('end_date'), '%Y-%m-%d').date()

#         Subscription.objects.create(
#             user=request.user,
#             gym_id=gym_id,
#             start_date=start_date,
#             end_date=end_date,
#             price=50.00  # Укажите цену
#         )
#         # Отображение успешной покупки
#         return render(request, 'subscriptions/success.html')
#     return render(request, 'subscriptions/purchase.html', {'gyms': gyms})


@login_required
def subscription_purchase(request, gym_id):
    """Страница покупки абонемента"""
    gym = get_object_or_404(Gym, pk=gym_id)
    discount = Discount.objects.filter (code = request.POST.get('discount')).first()
    
    if request.method == 'POST':
        # Логика создания абонемента
        start_date = datetime.now().date()
        end_date = start_date + timedelta(days=30)  # Абонемент на 30 дней
        subscription=Subscription.objects.create(
            user=request.user,
            gym=gym,
            start_date=start_date,
            end_date=end_date,
            price=gym.first_prise*(discount.discount_percentage/100) if discount is not None else gym.first_prise  # Цена абонемента
        )
        
        send_notification.delay(
                user_id=request.user.id,
                message=f"Вы оформили подписку на {subscription.gym.name}"
            )
        # Перенаправление в личный кабинет
        return render(request, 'subscriptions/success.html', {'gym': gym})
    return render(request, 'subscriptions/purchase.html', {'gym': gym})


class SubscriptionListView(APIView):
    """Список всех абонементов"""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        subscriptions = Subscription.objects.filter(user=request.user)
        serializer = SubscriptionSerializer(subscriptions, many=True)
        return Response(serializer.data)

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

    permission_classes = [IsAuthenticated]

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
