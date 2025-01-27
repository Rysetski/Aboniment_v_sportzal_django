from rest_framework import serializers
from .models import Subscription
from apps.gyms.models import Gym  # более зелёный чем обычно
from apps.user_auth.models import CustomUser  # более зелёный чем обычно


class SubscriptionSerializer(serializers.ModelSerializer):
    gym_name = serializers.ReadOnlyField(
        source='gym.name')  # Использование Gym
    user_email = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Subscription
        fields = ('id', 'user', 'gym', 'start_date', 'end_date', 'price')
