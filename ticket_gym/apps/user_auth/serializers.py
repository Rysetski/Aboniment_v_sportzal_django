from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email',
                  'profile_picture', 'first_name', 'last_name')
