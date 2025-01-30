from django.urls import path
from .views import subscription_purchase
from .views import subscription_list, SubscriptionListView, SubscriptionDetailView

urlpatterns = [
    path('my-subscriptions/', subscription_list, name='subscription-list-html'),

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



