# Generated by Django 3.1.2 on 2020-12-08 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_mascotas', '0014_auto_20201130_2334'),
        ('veterinario', '0013_auto_20201208_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estado_mascota',
            name='historia_clinica',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestion_mascotas.mascota'),
        ),
    ]
