"""User models."""

# Django
from django.db import models
from django.contrib.auth.models import User


class School(models.Model):
    """School model"""
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20,blank=True)
    director = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True) 

    def __str__(self):
        """return name school"""
        return self.name

class Student(models.Model):
    """Student model"""
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    school = models.ForeignKey(School,on_delete=models.CASCADE,blank=True,null=True)
    picture = models.ImageField(upload_to='users/picture/',blank=True,null=True)

    def __str__(self):
        """return username studen"""
        return self.user.username


class Teacher(models.Model):
    """Teacher model"""
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    schools = models.ManyToManyField(School)
    biography = models.TextField(blank=True)
    picture = models.ImageField(upload_to='users/picture/',blank=True,null=True)

    def __str__(self):
        """return username teacher"""
        return self.user.username
