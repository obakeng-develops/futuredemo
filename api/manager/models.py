from django.conf import settings
from django.db import models

class Requests(models.Model):
    """
    Requests to map all request by the manager to the client.
    """
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='request_manager', on_delete=models.CASCADE)
    client = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='request_client', on_delete=models.CASCADE)
    request_notes = models.TextField()
    request_date = models.DateTimeField(auto_now_add=True)
    isDone = models.BooleanField(default=False)

    def __str__(self):
        return str(self.request_date)
