from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Meta:
        indexes = (
            models.Index(fields=['last_name']),
            models.Index(fields=['first_name']),
        )
