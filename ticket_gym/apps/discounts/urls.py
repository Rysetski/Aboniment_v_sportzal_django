from django.urls import path
from .views import GymListView, GymDetailView

urlpatterns = [
    path('', GymListView.as_view(), name='gym-list'),
    path('<int:pk>/', GymDetailView.as_view(), name='gym-detail'),
]
