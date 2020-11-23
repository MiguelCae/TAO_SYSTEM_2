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
from django.contrib import admin, auth
from django.urls import path

from apps.adopcion import views as posts_views
from apps.gestion_mascotas import views as gest_mascotas
from apps.gestion_mascotas import views as gest_mascotas
#from apps.gestion_mascotas import views as pruebas, registro_mascota
from apps.gestion_mascotas import views as registro_mascota_view 
from apps.gestion_mascotas import views as mascota_edit
from apps.gestion_mascotas import views as mascota_delete 
from django.conf.urls import include

from apps.control_usuarios import views as send_email
from apps.gestion_mascotas import views as import_data

from apps.adopcion.views import mascotaListView



#Control de usuarios de usuarios
from apps.control_usuarios import views as user_views



urlpatterns = [

# Admin de Django    
    path('admin/', admin.site.urls),

#Url de pagina principal, publica
    path('',mascotaListView.as_view(), name='Home'),
    path('about/', posts_views.about),
    path('adopt-info/', posts_views.adopt_info),
    path('services/', posts_views.services),
    path('contact/', posts_views.contact),
    path('accounts/profile/', user_views.login_view, name='log'),
    path('accounts/register', user_views.Registro_view.as_view(), name ='registro'),
    


# Url's para administracion de la aplicación
    path('tao_log/', gest_mascotas.log),
    path('?next=/tao_admin/list/', gest_mascotas.mascota_list, name='list'),
    path('?next=/tao_admin/registro-mascota', gest_mascotas.registro_mascota_view, name='registro_mascota'),
    path('?next=/tao_admin/editar-mascota/<int:id>/', gest_mascotas.mascota_edit, name='editar_mascota'),
    path('tao_admin/eliminar-mascota/<int:id>/', gest_mascotas.mascota_delete, name='eliminar_mascota'),
    path('tao_admin/send_mail/', send_email.indexmail, name ='send_mail'),
    path('tao_admin/import_data/',import_data.importar, name='import_data'),


]

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
