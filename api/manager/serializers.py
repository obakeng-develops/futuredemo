from rest_framework import serializers
from .models import Requests

class RequestsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Requests
        fields = ['id', 'manager', 'client', 'request_notes', 'request_date', 'isDone']
