from django.contrib import admin

#Models
from .models import Profile, Rol

# Register your models here.

@admin.register(Profile)
class Profile_admin(admin.ModelAdmin):
    list_display = (
        'user',
        'telefono',
        'documento',
        'direccion',
        'ocupacion',
        
    )



admin.site.register(Rol)