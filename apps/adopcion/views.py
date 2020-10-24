from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def list_posts(request):
    return render(request, 'post_mascotas/index.html')

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

