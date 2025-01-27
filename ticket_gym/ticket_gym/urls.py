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
from django.urls import path, include
from apps.user_auth.views import home_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('auth/', include('apps.user_auth.urls')),  # URL-ы для авторизации
    path('gyms/', include('apps.gyms.urls')),  # URL-ы для спортзалов
    # URL-ы для абонементов
    path('subscriptions/', include('apps.subscriptions.urls')),
    path('discounts/', include('apps.discounts.urls')),  # URL-ы для скидок
    # URL-ы для уведомлений
    path('notifications/', include('apps.notifications.urls')),
]
