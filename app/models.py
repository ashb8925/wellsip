from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password, check_password

class UsersModel(AbstractUser):
    profile_picture = models.ImageField(upload_to='media/profile_pics/', blank=True, null=True)
