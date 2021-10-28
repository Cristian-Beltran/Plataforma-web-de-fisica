"""Posts app configuration"""
from django.apps import AppConfig


class PostsConfig(AppConfig):
    """Post app configure"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts'
    verbose_name='Posts'
