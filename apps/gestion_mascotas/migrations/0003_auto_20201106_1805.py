# Generated by Django 3.1.2 on 2020-11-06 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_mascotas', '0002_auto_20201106_0323'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='foto_mascota',
            field=models.ImageField(upload_to='static/img'),
        ),
    ]
