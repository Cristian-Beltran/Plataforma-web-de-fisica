"""Groups model"""

# Django
from django.db import models

# Models users

from users.models import Student, Teacher


class Group(models.Model):
    """Group models"""
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)
    created_at = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        """return name Group"""
        return self.name
