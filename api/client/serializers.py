from rest_framework import serializers
from .models import ClientGroup, Document, Membership

class ClientGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClientGroup
        fields = ['id', 'manager', 'client_group_name', 'clients']

class MembershipSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Membership
        fields = ['client', 'group', 'date_joined']

class DocumentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Document
        fields = ['document', 'client', 'manager', 'created_at', 'updated_at']