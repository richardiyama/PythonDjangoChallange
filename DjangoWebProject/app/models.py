"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=60, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)