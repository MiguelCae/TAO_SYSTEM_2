# Generated by Django 3.1.2 on 2020-12-01 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('veterinario', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estado_mascota',
            name='estado_mascota',
        ),
    ]
