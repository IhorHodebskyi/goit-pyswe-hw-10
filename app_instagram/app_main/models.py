from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Author(models.Model):
    fullname = models.CharField(max_length=255)
    born_date = models.CharField(max_length=255)
    born_location = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(User, blank=True, null=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.fullname


class Quote(models.Model):
    tags = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    quote = models.TextField()

    def __str__(self):
        return self.quote
