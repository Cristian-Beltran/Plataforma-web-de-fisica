"""Labs models"""
# Django
from django.db import models

# Users models
from users.models import Teacher, Student

# Groups models
from groups.models import Group 


class Lab(models.Model):
    """Post model"""
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="labs/photos")

    contain = models.TextField()
    visible = models.BooleanField()
    public = models.BooleanField()

    created_at = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    groups = models.ManyToManyField(Group)
    students = models.ManyToManyField(Student,through="NoteLab")
    def __str__(self):
        """return title  post"""
        return self.title

class NoteLab(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    lab = models.ForeignKey(Lab,on_delete=models.CASCADE)

    contain = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)