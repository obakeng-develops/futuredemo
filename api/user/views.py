from django.shortcuts import render
from rest_framework.serializers import Serializer
from rest_framework.views import APIView, set_rollback
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import CustomUser
from .serializers import CustomUserSerializer

# User API View
class CustomUserAPIView(generics.ListCreateAPIView):

    """
    List all users or create a new user.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

# User Detail View
class CustomUserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):

    """
    Retrieve, update or destroy user.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
