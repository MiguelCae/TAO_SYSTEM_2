from django import forms
from django.forms import ModelForm, Textarea, DateTimeInput, TextInput, Select, NumberInput, DateInput, HiddenInput


#Models
from .models import mascota

from functools import partial



class RegistroMascota(ModelForm):
    class Meta:
        model = mascota
       
    
        fields = (
            'nombre',
            'especie', 
            'raza',
            'tamaño',
            'sexo',
            'edad_aproximada',
            'fecha_rescate',
            'estado',
            'descripcion_mascota',
            'foto_mascota',
        )
        widgets = {
            'nombre':  TextInput(attrs={'class': 'form-control'}),
            'especie':  Select(attrs={'class': 'form-control'}),
            'raza' :  TextInput(attrs={'class': 'form-control'}),
            'tamaño':  Select(attrs={'class': 'form-control'}),
            'sexo':  Select(attrs={'class': 'form-control'}),
            'edad_aproximada' :  NumberInput(attrs={'class': 'form-control'}),
            'fecha_rescate': HiddenInput(attrs={
                'class': 'form-control datetimepicker-input',
                'data-target': '#datetimepicker1' 
                }),
            'estado':  Select(attrs={'class': 'form-control'}),
            'descripcion_mascota': Textarea(attrs={'class': 'form-control','cols': 40, 'rows': 5}),
            

        }
        
        

