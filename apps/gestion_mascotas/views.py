from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import ListView, CreateView
from django.urls import reverse

 #views class
from django.views.generic import ListView

#Model
from .models import mascota

#Form
from .forms import RegistroMascota

# Create your views here.

def log(request):
    log_in = "Login"
    return HttpResponse(log_in)

def mascota_list(request):
    QS_mascota = mascota.objects.all()
    contexto = {'mascotas' : QS_mascota}
    return render(request, 'desk.html', contexto)




def registro_mascota_view(request):
    if request.method == 'POST':
        form = RegistroMascota(request.POST or None)
        if form.is_valid():
            form.save()
    #context = {
            #'form': form
    #}
            return HttpResponseRedirect('list')
    else:
        form = RegistroMascota()
    return render (request,'formularios/formulario_mascota.html', {'form': form})

def mascota_edit(request, id):
    QS_mascota = mascota.objects.get(id = id)
    if request.method == 'GET':
        form = RegistroMascota(instance=QS_mascota)
    else:
        form = RegistroMascota(request.POST, instance=QS_mascota)
        if form.is_valid():
            form.save()
            return  redirect('list')
    return render (request,'formularios/formulario_mascota.html', {'form': form})

def mascota_delete(request, id):
    QS_mascota = mascota.objects.get(id = id)
    if request.method == 'POST':
        QS_mascota.delete()
        return  redirect('list')
    return render (request,'delete_mascota.html', {'QS_mascota': QS_mascota})
    
        



