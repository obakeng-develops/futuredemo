from django.urls import path, include
from .views import (
    RequestAPIView,
    RequestDetailAPIView
)

urlpatterns = [
    path("requests", RequestAPIView.as_view()),
    path("requests/client/<int:user_id>", RequestDetailAPIView.as_view())
]