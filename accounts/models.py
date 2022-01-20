from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    age = models.DateField(null=True)

    def __str__(self):
        return self.username