from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Enforce strict role tracking using distinct booleans
    is_owner = models.BooleanField(default=False)
    is_standard_user = models.BooleanField(default=False)
    
    # Enforce unique emails across the platform
    email = models.EmailField(unique=True, max_length=255)

    # Swap the primary login credential from username to email
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self) -> str:
        return f"{self.username} ({'Owner' if self.is_owner else 'User'})"