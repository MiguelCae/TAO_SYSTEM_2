from django.db import models

# Create your models here.
class persona(models.Model):
    documento = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=10)
    correo = models.EmailField(max_length=80)
    ciudad = models.CharField(max_length=50, null= True)
    direccion = models.CharField(max_length=50, null= True)
    ocupacion = models.CharField(max_length=50)
    rol = models.CharField(max_length=50)