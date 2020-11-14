from django.db import models

#django
from django.contrib.auth.models import User

# Create your models here.
# class persona(models.Model):
#   documento = models.IntegerField(primary_key=True)
#  nombre = models.CharField(max_length=50)
#   apellidos = models.CharField(max_length=50)
#   edad = models.IntegerField()
#    telefono = models.CharField(max_length=10)
#    correo = models.EmailField(max_length=80)
#   ciudad = models.CharField(max_length=50, null= True)
#   direccion = models.CharField(max_length=50, null= True)
#   ocupacion = models.CharField(max_length=50)
#   rol = models.CharField(max_length=50)


#Modelo proxy para gestion de usuarios 
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    telefono = models.CharField(max_length=10)
    documento = models.CharField(max_length=20, null=False)
    edad = models.IntegerField()
    ciudad = models.CharField(max_length=50, null= True)
    direccion = models.CharField(max_length=50, null= True)
    ocupacion = models.CharField(max_length=50)


#Modelo para Roles de usuarios
class Rol(models.Model):
    rol_user = models.OneToOneField(User,on_delete=models.CASCADE)
    rol = models.CharField(max_length=50 )

def __str__(self):
    #Return username
    return self.user.username

