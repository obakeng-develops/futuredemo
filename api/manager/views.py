from functools import partial
from django.db.models import query
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import Requests
from .serializers import RequestsSerializer, CreateRequestsSerializer

# Request API VIew
class RequestAPIView(generics.ListAPIView):
    """
    List all requests.
    """
    queryset = Requests.objects.filter(isDone=True)
    serializer_class = RequestsSerializer

# Create Request API View
class CreateRequestAPIView(generics.CreateAPIView):
    """
    Create new request.
    """
    queryset = Requests.objects.all()
    serializer_class = CreateRequestsSerializer

# Request Detail API View
class RequestDetailAPIView(generics.RetrieveUpdateDestroyAPIView):

    """
    Retrieve, update or destroy request.
    """
    queryset = Requests.objects.all()
    serializer_class = RequestsSerializer