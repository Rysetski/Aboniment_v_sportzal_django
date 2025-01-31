from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()  # <-- здесь Django сам подставит ваш CustomUser
        fields = ("username", "email") 
