"""
URL configuration for ticket_gym project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import (
    UserProfileView, RegisterView, GymListView, GymDetailView,
    SubscriptionListView, SubscriptionDetailView, DiscountListView, NotificationListView
)

urlpatterns = [
    # URLs для auth
    path('auth/profile/', UserProfileView.as_view(), name='user-profile'),
    path('auth/register/', RegisterView.as_view(), name='register'),

    # URLs для gyms
    path('gyms/', GymListView.as_view(), name='gym-list'),
    path('gyms/<int:pk>/', GymDetailView.as_view(), name='gym-detail'),

    # URLs для subscriptions
    path('subscriptions/', SubscriptionListView.as_view(),
         name='subscription-list'),
    path('subscriptions/<int:pk>/', SubscriptionDetailView.as_view(),
         name='subscription-detail'),

    # URLs для discounts
    path('discounts/', DiscountListView.as_view(), name='discount-list'),

    # URLs для notifications
    path('notifications/', NotificationListView.as_view(),
         name='notification-list'),
]
