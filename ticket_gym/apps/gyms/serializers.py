from rest_framework import serializers
from .models import Gym


class GymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gym
        fields = ('id', 'name', 'description',
                  'address', 'phone_number', 'image')
