from django.db import models
from apps.gestion_mascotas.models import mascota

# Create your models here.

class estado_mascota(models.Model):
    historia_clinica = models.OneToOneField(mascota,on_delete=models.CASCADE)
    r_historia_clinica = models.CharField(max_length=500, null=True)
    