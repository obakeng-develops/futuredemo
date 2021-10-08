from django.db import models
from django.conf import settings

from manager.models import Requests

class ClientGroup(models.Model):
    """
    A Client Group, with clients.
    """
    client_group_name = models.CharField(max_length=30)
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    clients = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='client_group', through='Membership')

    def __str__(self):
        return self.client_group_name


class Membership(models.Model):
    """
    Membership mapping.
    """
    client = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='client_name', on_delete=models.CASCADE)
    group = models.ForeignKey(ClientGroup, on_delete=models.CASCADE)
    date_joined = models.DateField(auto_now_add=True)

class Document(models.Model):
    """
    Document that stores all client documents.
    """
    document = models.TextField()
    client = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='document_client', on_delete=models.CASCADE)
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='document_manager', on_delete=models.CASCADE)
    request = models.ForeignKey(Requests, blank=True, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.document

