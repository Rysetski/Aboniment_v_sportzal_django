from django.contrib import admin
from .models import Subscription


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'gym', 'start_date', 'end_date', 'price')
    search_fields = ('user__username', 'gym__name')  # Поля для поиска
