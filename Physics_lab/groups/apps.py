"""Groups app configuration"""
from django.apps import AppConfig


class GroupsConfig(AppConfig):
    """Group app config"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'groups'
    verbose_name = 'Groups'
