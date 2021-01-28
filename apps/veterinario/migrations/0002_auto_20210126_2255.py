# Generated by Django 3.1.2 on 2021-01-27 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_mascotas', '0014_auto_20201130_2334'),
        ('veterinario', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estado_mascota',
            name='estado_mascota',
        ),
        migrations.AddField(
            model_name='estado_mascota',
            name='r_historia_clinica',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='estado_mascota',
            name='historia_clinica',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gestion_mascotas.mascota'),
        ),
    ]