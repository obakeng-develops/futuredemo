from rest_framework import serializers
from .models import Requests
from user.serializers import CustomUserSerializer

class RequestsSerializer(serializers.ModelSerializer):
    client = CustomUserSerializer()
    manager = CustomUserSerializer()

    class Meta:
        model = Requests
        fields = ['id', 'manager', 'client', 'request_notes', 'request_date', 'isDone']

class CreateRequestsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Requests
        fields = ['id', 'manager', 'client', 'request_notes', 'request_date', 'isDone']
        
