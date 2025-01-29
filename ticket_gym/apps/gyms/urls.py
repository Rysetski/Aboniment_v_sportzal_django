from django.urls import path
from .views import gym_list, GymDetailView

urlpatterns = [
    path('', gym_list, name='gym-list'),  # HTML страница с тренажёрными залами
    path('<int:pk>/', GymDetailView.as_view(), name='gym-detail'),  # для деталей зала
]
