# Generated by Django 3.1.2 on 2020-12-01 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_mascotas', '0012_auto_20201130_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='edad_aproximada',
            field=models.IntegerField(null=True),
        ),
    ]
