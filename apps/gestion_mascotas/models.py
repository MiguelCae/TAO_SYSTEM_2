from django.db import models

# Create your models here.
class mascota(models.Model):
    nombre = models.CharField(max_length=50)
    especie = models.CharField(max_length=50, null= True)
    raza = models.CharField(max_length=50, null= True)
    tamaño = models.CharField(max_length=50, null= True)
    sexo = models.CharField(max_length=10)
    edad_aproximada = models.IntegerField()
    fecha_rescate = models.DateField()
    estado = models.CharField(max_length=50, null= True)
    descripcion_mascota = models.CharField(max_length=50)
    foto_mascota = models.CharField(max_length=250)