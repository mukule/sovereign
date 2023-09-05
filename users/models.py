from django.db import models
from django.contrib.auth.models import AbstractUser
import os

# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    
    ACCESS_LEVEL_CHOICES = (
        ('system admin', 'system admin'),
        ('admin', 'admin'),
    )
    
    access_level = models.CharField(
        max_length=20,
        choices=ACCESS_LEVEL_CHOICES, null=True, blank=True
    )

    def image_upload_to(self, filename):
        return os.path.join('Users', self.username, filename)
    
    profile = models.ImageField(
        default='default/user.jpg',
        upload_to=image_upload_to
    )

    def __str__(self):
        return self.username