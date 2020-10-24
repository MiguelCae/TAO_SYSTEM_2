from django.db import models

# Create your models here.

class estado_mascota(models.Model):
    estado_mascota = models.CharField(max_length=50)
    historia_clinica =models.TextField(max_length=280)