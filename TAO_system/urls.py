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


# Posts de adopción de mascotas
from apps.adopcion.views import mascotaListView



#Veterinario
from apps.veterinario.views import  mascota_list_vet, date_historia_clinica, create_historia_clinica, vet_registro_mascota, vet_registro_list_mascota
# VetMascotaListView





#Control de usuarios de usuarios
from apps.control_usuarios import views as user_views

#Moidulo admin

from apps.admin.views import chart1
from apps.admin.views import DashboardView
from apps.admin.views import report, report_pdf_view

from apps.export.views import importar




urlpatterns = [

# Admin de Django    
    path('admin/', admin.site.urls),

#Url de pagina principal, publica
    path('',mascotaListView.as_view(), name='Home'),
    path('about/', posts_views.about),
    path('adopt-info/', posts_views.adopt_info),
    path('services/', posts_views.services),
    path('contact/', posts_views.contact),
    path('users/login/', user_views.login_view, name='login'),
    path('users/logout/', user_views.logout_view, name='logout'),
    path('users/signup/', user_views.signup_view, name='signup'),
    
    


# Url's para administracion de la aplicación

    path('tao_admin/list/', gest_mascotas.mascota_list, name='list'),
    path('tao_admin/registro-mascota', gest_mascotas.registro_mascota_view, name='registro_mascota'),
    path('tao_admin/editar-mascota/<int:id>/', gest_mascotas.mascota_edit, name='editar_mascota'),
    path('tao_admin/eliminar-mascota/<int:id>/', gest_mascotas.mascota_delete, name='eliminar_mascota'),
    path('tao_admin/send_mail/', send_email.indexmail, name ='send_mail'),
    # path('tao_admin/import_data/',import_data.importar, name='import_data'),

#  Modulo veterinario
    path('veterinario/',mascota_list_vet, name='list_vet'),
    # path('veterinario/historia_clinica/<int:id>/', VetMascotaListView, name='paciente'),
    path('veterinario/historia-clinica/<int:pk>', date_historia_clinica.as_view(), name='historia_clinica'),
    path('veterinario/historia-clinica-create', create_historia_clinica.as_view(), name='historia_clinica_create'),
    path('veterinario/registro-mascota', vet_registro_mascota, name= 'registro_mascota_veterinario'),
    path('veterinario/list-mascota', vet_registro_list_mascota, name= 'list_mascota_veterinario'),

# Modulo admin
    path('tao_admin/dashboard', chart1, name = 'dashboard'),
    path('tao_admin/dashboard/2', DashboardView, name = 'line_chart'),
    path('tao_admin/reports', report, name = 'reportes'),
    path('tao_admin/reports/print', report_pdf_view.as_view(), name = 'print_report'),
    path('tao_admin/import', importar, name = 'import'),


]

