from django.db import models

from apps.control_usuarios.models import persona
from apps.gestion_mascotas.models import mascota

# Create your models here.
class perfil_adoptante(models.Model):
    circulo_familiar = models.IntegerField()
    experiencia_mascotas = models.IntegerField()
    Persona = models.ForeignKey(persona, null=True, blank=True, on_delete=models.CASCADE)

class perfil_adoptar(models.Model):
    foto_adopcion = models.CharField(max_length=250)
    descripcion_adopcion = models.TextField(max_length=280)
    Mascota = models.OneToOneField(mascota, null=True, blank=True, on_delete=models.CASCADE)