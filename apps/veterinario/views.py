from django.shortcuts import render, redirect, HttpResponseRedirect
from apps.gestion_mascotas.models import mascota
from apps.veterinario.models import estado_mascota

from django.views import generic

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views.generic import  CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.gestion_mascotas.forms import RegistroMascota



from django.views.generic.edit import FormView

from .models import estado_mascota

from .forms import estado_mascota_form

from django.urls import reverse_lazy

# Create your views here.

@login_required
def mascota_list_vet(request):
    QS_mascota_v = mascota.objects.filter(estado__icontains='En tratamiento')
    contexto = {'mascotas' : QS_mascota_v}
    return render(request, 'veterinario/list_veterinario.html', contexto)

@login_required
def vet_registro_mascota(request):
    if request.method == 'POST':
        form = RegistroMascota(request.POST or None, request.FILES)
        fecha_rescate = request.POST.get('mail')
        if form.is_valid():
            form.save()
        return redirect('list_vet')
    else:
        form = RegistroMascota()
    return render(request, 'veterinario/registro_veterinario.html', {'form': form})


@login_required
def vet_registro_list_mascota(request):
    QS_mascota = mascota.objects.all()
    contexto = {'mascotas' : QS_mascota}
    return render(request, 'veterinario/list_registro_veterinario.html', contexto)



class date_historia_clinica(DetailView, UpdateView, CreateView, FormView, LoginRequiredMixin):
    model = mascota
    queryset = mascota.objects.all()
    template_name = 'veterinario/historia_c.html'
    context_object_name = 'paciente'
    form_class = estado_mascota_form
    success_url = reverse_lazy('list_vet')
    





class create_historia_clinica(CreateView):
    model = estado_mascota
    template_name = 'veterinario/historia_c.html'
    

# @login_required
# def VetMascotaListView(request, id):
#     QS_mascota_v = mascota.objects.get(id = id)
#     if request.method == 'POST':
#         Estado_mascota = estado_mascota.objects.create()
#         Estado_mascota = request.POST['historia_clinica']
#         Estado_mascota.save()
#         return redirect('list_vet')
#     return render(request, 'veterinario/historia_c.html',{'QS_mascota_v': QS_mascota_v} )

    