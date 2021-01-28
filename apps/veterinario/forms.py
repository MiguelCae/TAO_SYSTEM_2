from django import forms
from django.forms import ModelForm, Textarea


#Models
from .models import estado_mascota
from apps.gestion_mascotas.models import mascota



from functools import partial



class estado_mascota_form(ModelForm):
    class Meta:
        model = estado_mascota
       
    
        fields = (
            # 'historia_clinica',
            'r_historia_clinica',
        )
        widgets = {
            'r_historia_clinica': Textarea(attrs={'class': 'form-control','cols': 20, 'rows': 5}),
        }




