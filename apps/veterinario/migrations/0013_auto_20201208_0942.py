# Generated by Django 3.1.2 on 2020-12-08 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veterinario', '0012_auto_20201208_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estado_mascota',
            name='r_historia_clinica',
            field=models.CharField(max_length=500, null=True),
        ),
    ]