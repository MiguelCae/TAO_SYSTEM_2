# Generated by Django 3.1.2 on 2021-02-01 03:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_mascotas', '0014_auto_20201130_2334'),
        ('adopcion', '0003_perfil_adoptante_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil_adoptante',
            name='adopcion_mascota',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestion_mascotas.mascota'),
        ),
        migrations.AddField(
            model_name='perfil_adoptante',
            name='alergia_mascota',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='perfil_adoptante',
            name='antes_mascotas',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='perfil_adoptante',
            name='casa_apartemento',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='perfil_adoptante',
            name='casa_propia',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='perfil_adoptante',
            name='espacio_mascota',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='perfil_adoptante',
            name='lugar_seg_mascota',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='perfil_adoptante',
            name='mas_mascotas',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='perfil_adoptante',
            name='mascota_sola',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='perfil_adoptante',
            name='presupuesto_mascotas',
            field=models.BooleanField(null=True),
        ),
    ]
