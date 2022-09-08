from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(max_length=254, unique=True)
    role = models.TextField(
        'Роль',
        blank=True,
    )
    bio = models.TextField(
        'Биография',
        blank=True,
    )
