# Generated by Django 3.1.2 on 2020-11-15 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_mascotas', '0006_auto_20201115_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='edad_aproximada',
            field=models.FloatField(),
        ),
    ]