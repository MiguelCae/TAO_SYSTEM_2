from django.shortcuts import render
from django.http import HttpResponse
from apps.gestion_mascotas.models import mascota
from apps.adopcion.models import perfil_adoptante


from django.views import generic

# Create your views here.

# def list_posts(request):
#     QS_post = mascota.objects.all()
#     contexto = {'mascotas' : QS_post}
#     return render(request, 'post/post.html', contexto)


class mascotaListView(generic.ListView):
    model = mascota
    context_object_name = 'mascota'
    queryset = mascota.objects.filter(estado__icontains='En adopcion')
    template_name = "post/post.html"
    def adoptar(request):
        if request.method == 'POST':
            circulo_familiar = request.POST['cf']
            experiencia_mascotas = request.POST['em']
            hijos = request['hijos']
        return render(request, 'adopcion/form.html')



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

