from rest_framework import serializers
from .models import Discount


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ('id', 'code', 'description',
                  'discount_percentage', 'valid_from', 'valid_until')
