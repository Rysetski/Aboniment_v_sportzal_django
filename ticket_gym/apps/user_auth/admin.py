# apps/user_auth/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """Класс настроек для отображения CustomUser в админке."""
    
    # Поля, которые будут показаны в списке
    list_display = ("username", "email", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active")

    # Поля при редактировании существующего пользователя (основная вкладка)
    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
    )

    # Поля при создании нового пользователя (форма Add user)
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "password1", "password2", "is_staff", "is_active")}
        ),
    )

    search_fields = ("email", "username")
    ordering = ("email",)



# <form method="post" action="{% url 'logout' %}">
#             {% csrf_token %}
#               <button type="submit" class="animated-button-logaut-first logout-button">Нажми меня</button>
# </form>