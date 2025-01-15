from django.urls import path
from .views import SubscriptionListView, SubscriptionDetailView

urlpatterns = [
    path('', SubscriptionListView.as_view(), name='subscription-list'),
    path('<int:pk>/', SubscriptionDetailView.as_view(),
         name='subscription-detail'),
]
