from django import forms
from django.db.models import fields
from django.forms import ModelForm, Textarea, DateTimeInput, TextInput, Select, NumberInput, DateInput, HiddenInput, widgets
from django.forms.fields import BooleanField
from django import forms

#Models
from apps.adopcion.models import perfil_adoptante



class formulario_adopcion(forms.ModelForm):
    class Meta:
        model = perfil_adoptante

        fields=(
            'circulo_familiar',
            'experiencia_mascotas',
            'hijos',
            'casa_apartemento',
            'casa_propia',
            'lugar_seg_mascota',
            'espacio_mascota',
            'alergia_mascota',
            'antes_mascotas',
            'mas_mascotas',
            'presupuesto_mascotas',
            'mascota_sola',
            'acepta_terminos',
        )
        widgets={
            'circulo_familiar': TextInput(attrs={'class': 'form-control'}),
            'experiencia_mascotas': Select(attrs={'class': 'form-control'}),
            'hijos': Select(attrs={'class': 'form-control'}),
            'casa_apartemento': Select(attrs={'class': 'form-control'}),
            'casa_propia': Select(attrs={'class': 'form-control'}),
            'lugar_seg_mascota': Select(attrs={'class': 'form-control'}),
            'espacio_mascota': Select(attrs={'class': 'form-control'}),
            'alergia_mascota': Select(attrs={'class': 'form-control'}),
            'antes_mascotas': Select(attrs={'class': 'form-control'}),
            'mas_mascotas': Select(attrs={'class': 'form-control'}),
            'presupuesto_mascotas': Select(attrs={'class': 'form-control'}),
            'mascota_sola': Select(attrs={'class': 'form-control'}),
            'acepta_terminos': widgets.CheckboxInput(attrs={'class': 'form-control'}),
        }