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

    def follow(self, user):
        """Follow another user"""
        if user != self:
            self.following.add(user)

    def unfollow(self, user):
        """Unfollow another user"""
        if user in self.following.all():
            self.following.remove(user)

    def is_following(self, user):
        """Check if following a user"""
        return self.following.filter(id=user.id).exists()

    def __str__(self):
        return self.username
    