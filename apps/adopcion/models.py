from django.db import models
from django.db.models.fields import BooleanField, NullBooleanField


from apps.control_usuarios.models import Profile
from apps.gestion_mascotas.models import mascota

# Create your models here.
class perfil_adoptante(models.Model):
    circulo_familiar = models.IntegerField()
    experiencia_mascotas = models.IntegerField()
    hijos = models.IntegerField(null=True)
    casa_apartemento = models.IntegerField(null=True)
    casa_propia = models.IntegerField(null=True)
    lugar_seg_mascota = models.IntegerField(null=True)
    espacio_mascota = models.IntegerField(null=True)
    alergia_mascota = models.IntegerField(null=True)
    antes_mascotas = models.IntegerField(null=True)
    mas_mascotas = models.IntegerField(null=True)
    presupuesto_mascotas = models.IntegerField(null=True)
    mascota_sola = models.IntegerField(null=True)
    acepta_terminos = models.BooleanField(null=True)

    adopcion_mascota = models.ForeignKey(mascota, null=True, blank=True, on_delete=models.CASCADE)
    Profile = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)

class perfil_adoptar(models.Model):
    foto_adopcion = models.CharField(max_length=250)
    descripcion_adopcion = models.TextField(max_length=280)
    Mascota = models.OneToOneField(mascota, null=True, blank=True, on_delete=models.CASCADE)