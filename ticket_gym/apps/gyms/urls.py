from django.urls import path
from .views import gym_list, gym_detail

urlpatterns = [
    path('', gym_list, name='gym-list'),  # HTML страница с тренажёрными залами
    path('<int:pk>/', gym_detail, name='gym-detail'),  # для деталей зала
]
