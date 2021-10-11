from django.urls import path, include
from .views import (
    RequestAPIView,
    CreateRequestAPIView,
    RequestDetailAPIView
)

urlpatterns = [
    path("requests", RequestAPIView.as_view()),
    path("requests/create", CreateRequestAPIView.as_view()),
    path("requests/<int:pk>", RequestDetailAPIView.as_view())
]