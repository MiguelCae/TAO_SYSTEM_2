from django.db import models
from datetime import datetime



select_especie = [
    ('Gato', 'Gato'),
    ('Perro', 'Perro'),
]
select_tamaño = [
    ('Pequeño', 'Pequeño'),
    ('Mediano', 'Mediano'),
    ('Grande', 'Grande'),
]
select_sexo = [
    ('Hembra', 'Hembra'),
    ('Macho', 'Macho'),
]
select_estado = [
    ('En custodia','En custodia'),
    ('En tratamiento','En tratamiento'),
    ('En adopcion','En adopción'),
    ('Adoptado','Adoptado'),

]


# Create your models here.
class mascota(models.Model):
    nombre = models.CharField(max_length=50)
    especie = models.CharField(max_length=20,
        blank=False, null= False,
        choices=select_especie
        )
    raza = models.CharField(max_length=50, null= True)
    tamaño = models.CharField(max_length=20,
        blank=False, null= False,
        choices=select_tamaño
        )
    sexo = models.CharField(max_length=20,
        blank=False, null= False,
        choices=select_sexo
        )
    edad_aproximada = models.IntegerField(null=True)
    fecha_rescate = models.DateTimeField(null=True)
    estado = models.CharField(max_length=20,
        blank=False, null= False,
        choices=select_estado
        )
    descripcion_mascota = models.CharField(max_length=120)
    foto_mascota = models.ImageField(upload_to='static/img')
    created = models.DateTimeField(auto_now=True)

    


    def __str__(self):
       return self.nombre
    