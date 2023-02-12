from django.db import models
from django.contrib.auth.models import User


class Books(models.Model):
    name = models.CharField(max_length=100, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
