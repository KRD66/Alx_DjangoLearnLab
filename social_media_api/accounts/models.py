from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    bio = models.TextField(_("bio"), blank=True, null=True)
    profile_picture = models.ImageField(
        _("profile picture"), 
        upload_to='profile_pics/', 
        blank=True, 
        null=True
    )
    followers = models.ManyToManyField(
        'self',
        symmetrical=False,  # If user A follows B, B doesn't automatically follow A
        blank=True,
        related_name='following'
    )

    def __str__(self):
        return self.username
    