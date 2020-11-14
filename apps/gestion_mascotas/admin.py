from django.contrib import admin

#Models gestion mascota
from .models import mascota

# Register your models here.
@admin.register(mascota)
class Registro_mascotasa_admin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'raza',
        'tamaño',
        'sexo',
        'edad_aproximada',
        'created',
    
    )
    search_fields = (
         'nombre',
        'raza',
        'tamaño',
        'sexo',
        'edad_aproximada',
        'created',
    
    )
    
   