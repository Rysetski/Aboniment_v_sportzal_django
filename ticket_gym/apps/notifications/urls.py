from django.urls import path
from .views import NotificationListView, NotificationDetailView, MarkNotificationAsReadView

urlpatterns = [
    path('', NotificationListView.as_view(), name='notification-list'),
    path('<int:pk>/', NotificationDetailView.as_view(),
         name='notification-detail'),
    path('<int:pk>/mark-as-read/', MarkNotificationAsReadView.as_view(),
         name='notification-mark-as-read'),
]
