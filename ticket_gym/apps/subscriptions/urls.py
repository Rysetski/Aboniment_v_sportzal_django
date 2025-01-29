from django.urls import path
from .views import subscription_purchase
from .views import SubscriptionListView, SubscriptionDetailView

urlpatterns = [
   
    
    path('', SubscriptionListView.as_view(), name='subscription-list'),
    path('<int:pk>/', SubscriptionDetailView.as_view(),
         name='subscription-detail'),
    path('<int:gym_id>/purchase/', subscription_purchase, name='subscription_purchase'),
    
    
    # path('purchase/<int:gym_id>/', subscription_purchase,
    #      name='subscription-purchase'),
]
