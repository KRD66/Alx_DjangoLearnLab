from django.contrib.auth.models import AbstractUser


from django.db import models

class CustomUser(AbstractUser):  # Ensure this class exists
    email = models.EmailField(unique=True)
