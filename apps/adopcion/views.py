from django.shortcuts import render
from django.http import HttpResponse
from apps.gestion_mascotas.models import mascota

# Create your views here.

def list_posts(request):
    QS_post = mascota.objects.all()
    contexto = {'mascotas' : QS_post}
    return render(request, 'post/post.html', contexto)

def about(request):
    about_us = "Sobre nosotros"
    return HttpResponse(about_us)

def services(request):
    serv = "Servicios"
    return HttpResponse(serv)

def contact(request):
    cont = "Contacto"
    return HttpResponse(cont)

def adopt_info(request):
    info = "Informacion adopcion"
    return HttpResponse(info)

