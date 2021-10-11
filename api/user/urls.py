from django.urls import path, include
from .views import (
    CustomUserAPIView,
    CustomUserDetailAPIView,
)

urlpatterns = [
    path("", CustomUserAPIView.as_view()),
    path("<int:pk>", CustomUserDetailAPIView.as_view()),
]