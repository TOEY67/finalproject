# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True)  
    birthday = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')