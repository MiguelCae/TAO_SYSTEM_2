from django.shortcuts import render
import json
from django.core import serializers
from apps.gestion_mascotas.models import mascota

# Create your views here.

def chart1(request):
    # adopcion_data = serializers.serialize("json", mascota.objects.all(), fields=('pk'))
    adopcion_data = mascota.objects.filter(estado__icontains='En adopcion').count()
    custodia_data = mascota.objects.filter(estado__icontains='En custodia').count()
    tratamiento_data = mascota.objects.filter(estado__icontains='En tratamiento').count()
    adoptado_data = mascota.objects.filter(estado__icontains='Adoptado').count()
    context = {
        "json" : adopcion_data,
        "json2": custodia_data,
        "json3": tratamiento_data,
        "json4": adoptado_data,

        }
    return render(request, 'Graficos/charts.html', context)
