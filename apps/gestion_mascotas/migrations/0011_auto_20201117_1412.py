# Generated by Django 3.1.2 on 2020-11-17 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_mascotas', '0010_auto_20201115_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='descripcion_mascota',
            field=models.CharField(max_length=120),
        ),
    ]