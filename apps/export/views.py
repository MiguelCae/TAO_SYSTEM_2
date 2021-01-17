from django.shortcuts import render, redirect
from apps.gestion_mascotas.models import mascota
from import_export import resources
from django.contrib import messages

from django.http import HttpResponseRedirect

from tablib import Dataset

class mascota_import(resources.ModelResource):
    class Meta:
        model = mascota
        exclude = ('foto_mascota')

def importar(request):
    if request.method == 'POST':
        form = mascota_import()
        dataset = Dataset()
        nuevas_mascotas = request.FILES['xlsfile']
        imported_data = dataset.load(nuevas_mascotas.read())
        result = form.import_data(dataset, dry_run=True)
        if not result.has_errors():
            form.import_data(dataset, dry_run=False)
    return render(request, 'import/import.html')


# Create your views here.
