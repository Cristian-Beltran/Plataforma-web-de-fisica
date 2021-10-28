"""Posts admin class"""
# Django
from django.contrib import admin
# Models
from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post admin configure"""
    list_display = ('title','photo','visible','public')
    search_fields = ('title','teacher')
    list_filter = ('visible','public')