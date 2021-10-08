from django.urls import path, include
from .views import (
    ClientGroupAPIView,
    ClientGroupDetailAPIView,
    MembershipAPIView,
    MembershipDetailAPIView,
    DocumentAPIView,
    DocumentDetailAPIView
)

urlpatterns = [
    path("groups/", ClientGroupAPIView.as_view()),
    path("groups/member/<int:user_id>/", ClientGroupDetailAPIView.as_view()),
    path("membership/manager/<int:manager_id>", MembershipDetailAPIView.as_view()),
    path("memberships/", MembershipAPIView.as_view()),
    path("documents/", DocumentAPIView.as_view()),
    path("documents/client/<int:client_id>", DocumentDetailAPIView.as_view())
]