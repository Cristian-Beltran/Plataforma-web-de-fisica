"""Labs forms"""
# Django 
from django import forms
# Models
from labs.models import Lab 
from groups.models import Group

class LabForm(forms.ModelForm):
    """Post model form."""
    groups = forms.ModelMultipleChoiceField(queryset=Group.objects.all(),widget=forms.CheckboxSelectMultiple(attrs={'class':'input'}))
    class Meta:
        model = Lab 
        fields = ('title','photo','contain','visible','public','teacher','groups')

class FilterLabForm(forms.Form):
    title = forms.CharField()
    grupo = forms.CharField() 