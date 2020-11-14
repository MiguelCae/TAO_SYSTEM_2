"""TAO_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from apps.adopcion import views as posts_views
from apps.gestion_mascotas import views as gest_mascotas
from apps.gestion_mascotas import views as gest_mascotas
#from apps.gestion_mascotas import views as pruebas, registro_mascota
from apps.gestion_mascotas import views as mascota_list
from apps.gestion_mascotas import views as registro_mascota_view 
from apps.gestion_mascotas import views as mascota_edit
from apps.gestion_mascotas import views as mascota_delete 


#Control de usuarios de usuarios
from apps.control_usuarios import views as user_views



urlpatterns = [

# Admin de Django    
    path('admin/', admin.site.urls),

#Url de pagina principal, publica
    path('', posts_views.list_posts),
    path('about/', posts_views.about),
    path('adopt-info/', posts_views.adopt_info),
    path('services/', posts_views.services),
    path('contact/', posts_views.contact),
    path('login/', user_views.login_view, name='login'),
    


# Url's para administracion de la aplicación
    path('tao_log/', gest_mascotas.log),
    path('tao_admin/list/', gest_mascotas.mascota_list, name='list'),
    path('tao_admin/registro-mascota', gest_mascotas.registro_mascota_view, name='registro_mascota'),
    path('tao_admin/editar-mascota/<int:id>/', gest_mascotas.mascota_edit, name='editar_mascota'),
    path('tao_admin/eliminar-mascota/<int:id>/', gest_mascotas.mascota_delete, name='eliminar_mascota'),





]
