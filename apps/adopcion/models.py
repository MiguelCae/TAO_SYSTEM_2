from django.db import models
from django.db.models.fields import BooleanField, NullBooleanField


from apps.control_usuarios.models import Profile
from apps.gestion_mascotas.models import mascota

# Create your models here.

select=[
    (1 ,'Sí'),
    (2 ,'No')
]




class perfil_adoptante(models.Model):
    circulo_familiar = models.IntegerField()
    experiencia_mascotas = models.IntegerField(choices=select)
    hijos = models.IntegerField(null=True, choices=select)
    casa_apartemento = models.IntegerField(null=True, choices=select)
    casa_propia = models.IntegerField(null=True, choices=select)
    lugar_seg_mascota = models.IntegerField(null=True, choices=select)
    espacio_mascota = models.IntegerField(null=True, choices=select)
    alergia_mascota = models.IntegerField(null=True, choices=select)
    antes_mascotas = models.IntegerField(null=True, choices=select)
    mas_mascotas = models.IntegerField(null=True, choices=select)
    presupuesto_mascotas = models.IntegerField(null=True, choices=select)
    mascota_sola = models.IntegerField(null=True, choices=select)
    acepta_terminos = models.CharField(null=True, max_length=5)

    adopcion_mascota = models.ForeignKey(mascota, null=True, blank=True, on_delete=models.CASCADE)
    Profile = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.circulo_familiar

class perfil_adoptar(models.Model):
    foto_adopcion = models.CharField(max_length=250)
    descripcion_adopcion = models.TextField(max_length=280)
    Mascota = models.OneToOneField(mascota, null=True, blank=True, on_delete=models.CASCADE)

