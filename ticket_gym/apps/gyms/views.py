from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Gym
from .serializers import GymSerializer
from rest_framework.permissions import IsAuthenticated



@login_required
def gym_list(request):
    gyms = Gym.objects.all()  # Получаем все тренажёрные залы
    return render(request, 'gyms/gyms.html', {'gyms': gyms})


class GymListView(APIView):
    """Список всех спортзалов"""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        gyms = Gym.objects.all()
        serializer = GymSerializer(gyms, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GymSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GymDetailView(APIView):
    """Детали конкретного спортзала"""
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        gym = get_object_or_404(Gym, pk=pk)
        serializer = GymSerializer(gym)
        return Response(serializer.data)

    def put(self, request, pk):
        gym = get_object_or_404(Gym, pk=pk)
        serializer = GymSerializer(gym, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        gym = get_object_or_404(Gym, pk=pk)
        gym.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
