"""Labs admin class"""
# Django
from django.contrib import admin

# Models
from labs.models import Lab,NoteLab

@admin.register(Lab)
class LabAdmin(admin.ModelAdmin):
    """Lab admin configure"""
    list_display = ('title','photo','visible','public')
    search_fields = ('title','teacher')
    list_filter = ('visible','public')


@admin.register(NoteLab)
class NoteLab(admin.ModelAdmin):
    """NoteLab admin configure"""
    list_display = ('student','lab','created_at','modified')
    search_fields = ('student','lab')
    list_filter = ('student','lab')

