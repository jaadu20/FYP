# users/urls.py
from django.urls import path
from .views import (
    SignupView,
    MyTokenObtainPairView,
    ForgotPasswordView,
)

urlpatterns = [
    path('auth/signup/', SignupView.as_view(), name='signup'),
    path('auth/login/', MyTokenObtainPairView.as_view(), name='login'),
    path('auth/forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
]
    