from django.urls import path
from .views import discount_list_html, DiscountListView, DiscountDetailView

urlpatterns = [
    # 1) Функция-представление, отдаёт HTML
    path('', discount_list_html, name='discount-list'),
    
    # 2) Класс-представление (DRF), отдаёт JSON
    path('api/', DiscountListView.as_view(), name='discount-list-api'),
    path('api/<int:pk>/', DiscountDetailView.as_view(), name='discount-detail-api'),
]
