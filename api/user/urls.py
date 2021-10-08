from django.urls import path, include
from .views import (
    CustomUserAPIView,
    CustomUserDetailAPIView,
    ProfileAPIView,
    ProfileDetailAPIView
)

urlpatterns = [
    path("", CustomUserAPIView.as_view()),
    path("<int:user_id>", CustomUserDetailAPIView.as_view()),
    path("profile/all", ProfileAPIView.as_view()),
    path("profile/<int:user_id>", ProfileDetailAPIView.as_view())
]