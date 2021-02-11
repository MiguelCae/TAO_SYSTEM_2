from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse
from apps.gestion_mascotas.models import mascota
from apps.adopcion.models import perfil_adoptante
from apps.control_usuarios.models import Profile
# form
from apps.adopcion.forms import formulario_adopcion

import pdb

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


@login_required
def adoptar(request, id):
    queryset = mascota.objects.get(id=id)

    if request.method == 'POST':
        form = formulario_adopcion(request.POST)
        fecha_rescate = request.POST.get('mail')
        if form.is_valid():
            try:
                form.save()
            except:
                print('El error')
        return redirect('Home')
    else:
        form = formulario_adopcion()
    context = {
        'form_adopcion': form,
        'queryset': queryset
    }
    return render(request, 'adopcion/form_adopcion.html', context)


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
