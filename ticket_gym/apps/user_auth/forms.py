from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

class CustomUserCreationForm(UserCreationForm):
    
    email = forms.EmailField(required=True)
    class Meta:
        model = get_user_model()  
        # <-- здесь Django сам подставит ваш CustomUser
        
        fields = ("username", "email", "password1", "password2") 
