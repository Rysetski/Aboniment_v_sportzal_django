from django.urls import path
from .views import NotificationListView, NotificationDetailView, MarkNotificationAsReadView, notification_list, notification_list, cheker_notifications


urlpatterns = [
    path('', notification_list, name='notification-list'),
    path('notifications/chek/<int:pk>/', cheker_notifications, name='cheker_notifications'),
    path('api/', NotificationListView.as_view(), name='notification-list-api'),
    path('api/<int:pk>/', NotificationDetailView.as_view(),
         name='notification-detail'),
    path('api/<int:pk>/mark-as-read/', MarkNotificationAsReadView.as_view(),
         name='notification-mark-as-read'),
    
]

# cheker_notifications
#     # 1) Функция-представление, отдаёт HTML
#     path('', discount_list_html, name='discount-list'),
    
#     # 2) Класс-представление (DRF), отдаёт JSON
#     path('api/', DiscountListView.as_view(), name='discount-list-api'),
#     path('api/<int:pk>/', DiscountDetailView.as_view(), name='discount-detail-api'),