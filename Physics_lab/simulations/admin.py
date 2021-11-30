from django.contrib import admin

# Register your models here.

# Models
from simulations.models import Simulation 

@admin.register(Simulation)
class LabAdmin(admin.ModelAdmin):
    """Lab admin configure"""
    list_display = ('title','photo')
    search_fields = ('title',)

