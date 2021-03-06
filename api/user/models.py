from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from client.models import ClientGroup

from .managers import CustomUserManager


class CustomUser(AbstractUser):

    """
    Custom User mapping. Replaces username with email.
    """

    ROLE_CHOICES = [
        ('M', 'Manager'),
        ('C', 'Client')
    ]

    username = None
    email = models.EmailField(_('email address'), unique=True)
    role = models.CharField(max_length=1, choices=ROLE_CHOICES)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email