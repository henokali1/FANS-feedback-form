from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    id_number = models.PositiveIntegerField(default=0)
    