"""Post forms"""
# Django 
from django import forms

# Models

from posts.models import Post
from groups.models import Group

class PostForm(forms.ModelForm):
    """Post model form."""
    groups = forms.ModelMultipleChoiceField(queryset=Group.objects.all(),widget=forms.CheckboxSelectMultiple(attrs={'class':'input'}))
    class Meta:
        model = Post
        fields = ('title','photo','contain','visible','public','teacher','groups')
    