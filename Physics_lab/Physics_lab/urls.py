# DJango
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
# Views
from Physics_lab import views as local_views
from labs import views as labs_views
from posts import views as posts_views
from simulations import views as  simulations_views 
from users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',local_views.index,name='index'),
    
    path('users/login/',users_views.login_view,name='login'),
    path('users/logout/',users_views.logout_view,name='logout'),
    path('users/signup/',users_views.signup_view,name='signup'),
    path('users/perfil/student/',users_views.perfil_student_view,name='perfil_student'),
    path('users/perfil/teacher/',users_views.perfil_teacher_view,name='perfil_teacher'),
    path('users/perfil/student/update/',users_views.update_student_view,name='update_student'),
    path('users/perfil/teacher/update/',users_views.update_teacher_view,name='update_teacher'),


    path('posts/create/',posts_views.create_post_view,name='create_post'),
    path('posts/list/',posts_views.list_post_view,name='posts'),
    path('posts/post/<str:id>',posts_views.post_view,name='post'),

    path('labs/list/',labs_views.list_lab_view,name='labs'),
    path('labs/create/',labs_views.create_lab_view,name='create_lab'),
    path('labs/post/<str:id>/',labs_views.lab_view,name='lab'),

    path('simulations/list/',simulations_views.list_simulation_view,name='simulations'),
    path('simulations/<str:id>/',simulations_views.simulation_view,name='simulation'),


] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
