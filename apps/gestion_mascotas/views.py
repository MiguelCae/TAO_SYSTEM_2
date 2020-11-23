from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import ListView, CreateView
from django.urls import reverse

from .sources import Mascota_resource

# Carga inicial de datos
from tablib import Dataset 


from django.contrib import messages

#Login required
from django.contrib.auth.decorators import login_required

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

@login_required
def mascota_list(request):
    QS_mascota = mascota.objects.all()
    contexto = {'mascotas' : QS_mascota}
    return render(request, 'desk.html', contexto)



@login_required
def registro_mascota_view(request):
    if request.method == 'POST':
        form = RegistroMascota(request.POST or None, request.FILES)
        fecha_rescate = request.POST.get('mail')
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('list')
    else:
        form = RegistroMascota()
    return render (request,'formularios/formulario_mascota.html', {'form': form})

@login_required
def mascota_edit(request, id):
    QS_mascota = mascota.objects.get(id = id)
    if request.method == 'GET':
        form = RegistroMascota(instance=QS_mascota)
    else:
        form = RegistroMascota(request.POST,request.FILES,instance=QS_mascota)
        if form.is_valid():
            form.save()
            return  redirect('list')
    return render (request,'formularios/formulario_mascota.html', {'form': form})
    
@login_required
def mascota_delete(request, id):
    QS_mascota = mascota.objects.get(id = id)
    if request.method == 'POST':
        QS_mascota.delete()
        return  redirect('list')
    return render (request,'delete_mascota.html', {'QS_mascota': QS_mascota})


# Carga inicial de datos
def importar(request):
    if request.method == 'POST':
      MascotaResource = Mascota_resource()
      dataset =Dataset()
      nuevas_mascotas = request.FILES['xlsfile']
      imported_data = dataset.load(nuevas_mascotas.read())
      result = MascotaResource.import_data(dataset, dry_run=True)
      if not result.has_errors():
          MascotaResource.import_data(dataset, dry_run=False)
    return render(request, 'carga_datos.html')  







    
        



