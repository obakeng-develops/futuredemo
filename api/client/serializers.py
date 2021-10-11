from django.db.models import manager
from rest_framework import serializers

from user.serializers import CustomUserSerializer
from .models import ClientGroup, Document, Membership

class ClientGroupSerializer(serializers.ModelSerializer):
    manager = CustomUserSerializer()

    class Meta:
        model = ClientGroup
        fields = ['id', 'manager', 'client_group_name', 'clients']

class CreateClientGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClientGroup
        fields = ['id', 'manager', 'client_group_name', 'clients']

class MembershipSerializer(serializers.ModelSerializer):
    client = CustomUserSerializer()
    group = ClientGroupSerializer()
    
    class Meta:
        model = Membership
        fields = ['client', 'group', 'date_joined']

class DocumentSerializer(serializers.ModelSerializer):
    client = CustomUserSerializer()
    manager = CustomUserSerializer()
    
    class Meta:
        model = Document
        fields = ['id', 'document', 'client', 'manager', 'created_at', 'updated_at']

class CreateDocumentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Document
        fields = ['document', 'client', 'manager', 'created_at', 'updated_at']