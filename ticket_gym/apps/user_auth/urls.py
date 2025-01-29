from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from .views import UserProfileView, RegisterView, home_page


urlpatterns = [
    path('', home_page, name='home'),
    path('login/', LoginView.as_view(template_name='user_auth/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('register/', RegisterView.as_view(),
         name='register'),  # user-register
]
