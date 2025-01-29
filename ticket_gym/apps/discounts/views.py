from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Discount
from .serializers import DiscountSerializer
from django.shortcuts import render


@login_required
def discount_list_html(request):
    discounts = Discount.objects.all()  # Получаем все скидки
    return render(request, 'discounts/discounts_list.html', {'discounts': discounts})


class DiscountListView(APIView):
    """Список всех доступных скидок"""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        discounts = Discount.objects.all()
        serializer = DiscountSerializer(discounts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DiscountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DiscountDetailView(APIView):
    """Детали скидки"""
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        discount = get_object_or_404(Discount, pk=pk)
        serializer = DiscountSerializer(discount)
        return Response(serializer.data)

    def put(self, request, pk):
        discount = get_object_or_404(Discount, pk=pk)
        serializer = DiscountSerializer(discount, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        discount = get_object_or_404(Discount, pk=pk)
        discount.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # проверка на момент создания чтобы не было пересечений
    # и промежуточную таблицу создать
