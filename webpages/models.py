from django.db import models

# Create your models here.


class ContactModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField()

    def __str__(self):
        return f'{self.name}'