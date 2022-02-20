from django.db import models
from django.urls import reverse

# Create your models here.

class Contact(models.Model):

    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.phone} | {self.id}"


class Feedback(models.Model):

    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    comment = models.TextField()
    agree = models.BooleanField(default=False)


    def __str__(self):
        return self.name