"""Groups admin class"""
# Django
from django.contrib import admin
# Models

from groups.models import Group

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    """Group Admin"""
    list_display = ('name','teacher','created_at')
    search_fields = ('name','teacher')
    list_filter = ('teacher__user','created_at')
