"""Labs app configuration"""
from django.apps import AppConfig


class LabsConfig(AppConfig):
    """lab app configuration"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'labs'
    verbose_name = 'Labs'
