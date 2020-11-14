from django import forms
from django.forms import ModelForm


#Models
from .models import mascota




class RegistroMascota(ModelForm):
    class Meta:
        model = mascota
        fields = [
            'nombre',
            'especie', 
            'raza',
            'tamaño',
            'sexo',
            'edad_aproximada',
            'fecha_rescate',
            'estado',
            'descripcion_mascota',
            #'foto_mascota',
            ]
        

