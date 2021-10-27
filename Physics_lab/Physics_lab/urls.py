# DJango
from django.contrib import admin
from django.urls import path
# Views
from Physics_lab import views as local_views
from labs import views as labs_views
from posts import views as posts_views
from simulations import views as  simulations_views 

urlpatterns = [
    path('admin/', admin.site.urls),
]
