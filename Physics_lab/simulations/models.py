"""Simulate models"""
# Django
from django.db import models

class Simulation(models.Model):
    """Post model"""
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="labs/photos")

    contain = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        """return title  post"""
        return self.title


