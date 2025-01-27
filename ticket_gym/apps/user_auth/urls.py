from django.urls import path
from .views import UserProfileView, RegisterView, home_page


urlpatterns = [
    path('', home_page, name='home'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('register/', RegisterView.as_view(),
         name='register'),  # user-register
]
