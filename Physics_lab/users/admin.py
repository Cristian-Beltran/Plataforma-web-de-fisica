"""User admin class"""
# Django
from django.contrib import admin

# Models
from users.models import School,Student,Teacher

# Register your models here.
@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    """School admin"""
    list_display = ('name','director','address','modified')
    list_display_links = ('name','director')
    search_fields = ('name','director')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    """Student admin"""
    list_display = ('user','picture')
    list_display_links = ('user','picture')
    search_fields = ('user__email','user__first_name','user__last_name')
    list_filter = ('school','user__last_login')

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    """Teacher admin"""
    list_display = ('user','picture')
    list_display_links = ('user','picture')
    search_fields = ('user__email','user__first_name','user__last_name')
    list_filter = ('schools','user__last_login')
