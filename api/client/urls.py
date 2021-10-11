from django.urls import path, include
from .views import (
    ClientGroupAPIView,
    ClientGroupDetailAPIView,
    CreateClientGroupAPIView,
    MembershipAPIView,
    MembershipDetailAPIView,
    DocumentAPIView,
    CreateDocumentAPIView,
    DocumentDetailAPIView
)

urlpatterns = [
    path("groups/", ClientGroupAPIView.as_view()),
    path("groups/create", CreateClientGroupAPIView.as_view()),
    path("groups/manager/<int:manager_id>/", ClientGroupDetailAPIView.as_view()),
    path("membership/manager/<int:manager_id>", MembershipDetailAPIView.as_view()),
    path("memberships/", MembershipAPIView.as_view()),
    path("documents/", DocumentAPIView.as_view()),
    path("documents/create", CreateDocumentAPIView.as_view()),
    path("documents/<int:pk>", DocumentDetailAPIView.as_view())
]