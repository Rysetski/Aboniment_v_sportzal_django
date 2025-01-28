from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required  # Добавлен импорт
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from .serializers import UserSerializer







@login_required
def home_page(request):
    return render(request, 'home.html', {
        'title': 'Главная страница',
        'sections': [
            {'name': 'Тренажёрные залы', 'url': '/gyms/'},
            {'name': 'Скидки', 'url': '/discounts/'},
            {'name': 'Уведомления', 'url': '/notifications/'},
            {'name': 'Личный кабинет', 'url': '/subscriptions/'},
        ]
    })


class UserProfileView(APIView):
    """Отображение профиля пользователя"""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)


class RegisterView(APIView):
    """Регистрация нового пользователя"""

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
