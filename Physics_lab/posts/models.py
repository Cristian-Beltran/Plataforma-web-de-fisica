"""Posts models"""

# Django
from django.db import models

# Users models
from users.models import Teacher

# Groups models
from groups.models import Group

class Post(models.Model):
    """Post model"""
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="posts/photos")

    contain = models.TextField()
    visible = models.BooleanField()
    public = models.BooleanField()

    created_at = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    groups = models.ManyToManyField(Group)
    def __str__(self):
        """return title  post"""
        return self.title