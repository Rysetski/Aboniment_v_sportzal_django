from django.urls import path
from .views import subscription_purchase
from .views import subscription_list, SubscriptionListView, SubscriptionDetailView

urlpatterns = [
    # HTML-версия личного кабинета:
    path('my-subscriptions/', subscription_list, name='subscription-list-html'),

    # DRF (API) версии:
    path('', SubscriptionListView.as_view(), name='subscription-list'),
    path('<int:pk>/', SubscriptionDetailView.as_view(), name='subscription-detail'),
    path('<int:gym_id>/purchase/', subscription_purchase, name='subscription_purchase'),

]
# urlpatterns = [
   
#     path('', subscription_list, name='subscription-list'),
    
#     path('api/', SubscriptionListView.as_view(), name='subscription-list-api'),
#     path('<int:pk>/', SubscriptionDetailView.as_view(),
#          name='subscription-detail-api'),
#     path('<int:gym_id>/purchase/', subscription_purchase, name='subscription_purchase'),
# ]





# urlpatterns = [
#     path('', notification_list, name='notification-list'),
#     path('notifications/chek/<int:pk>/', cheker_notifications, name='cheker_notifications'),
#     path('api/', NotificationListView.as_view(), name='notification-list-api'),
#     path('api/<int:pk>/', NotificationDetailView.as_view(),
#          name='notification-detail'),
#     path('api/<int:pk>/mark-as-read/', MarkNotificationAsReadView.as_view(),
#          name='notification-mark-as-read'),