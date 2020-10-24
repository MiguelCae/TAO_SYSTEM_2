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
from apps.gestion_mascotas import views as pruebas

urlpatterns = [

# Admin de Django    
    path('admin/', admin.site.urls),

#Url de pagina principal, publica
    path('', posts_views.list_posts),
    path('about/', posts_views.about),
    path('adopt-info/', posts_views.adopt_info),
    path('services/', posts_views.services),
    path('contact/', posts_views.contact),


# Url's para administracion de la aplicación
    path('tao_log/', gest_mascotas.log),

    path('tao_admin/', gest_mascotas.workflow),

    #Pruebas templates
    path('tao_admin/pruebas',gest_mascotas.pruebas), 


    
]
