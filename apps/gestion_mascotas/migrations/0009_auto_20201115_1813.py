# Generated by Django 3.1.2 on 2020-11-15 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_mascotas', '0008_auto_20201115_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='fecha_rescate',
            field=models.DateField(),
        ),
    ]
