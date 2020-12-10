from django.contrib import admin
from .models import estado_mascota

# Register your models here.

@admin.register(estado_mascota)
class estado_mascota_admin(admin.ModelAdmin):
    list_display = (
        'r_historia_clinica',
    )
