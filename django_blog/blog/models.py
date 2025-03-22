from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone  # Import timezone for date handling

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)  
    created_at = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(default=timezone.now)  # Add this field

    def __str__(self):
        return self.title
