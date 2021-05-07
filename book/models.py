from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField()
    uploaded_at = models.DateTimeField(
        default=timezone.now
    )
    ISBN = models.TextField()
    Author = models.TextField()
    def __str__(self):
        return f'{self.name}'
