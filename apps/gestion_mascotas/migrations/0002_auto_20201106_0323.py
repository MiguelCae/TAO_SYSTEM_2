# Generated by Django 3.1.2 on 2020-11-06 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_mascotas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='sexo',
            field=models.IntegerField(choices=[(1, 'Hembra'), (2, 'Macho')]),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='tamaño',
            field=models.IntegerField(choices=[(1, 'Pequeño'), (2, 'Mediano'), (3, 'Grande')]),
        ),
    ]
