# Generated by Django 3.1.2 on 2020-10-16 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control_usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='persona',
            old_name='direccon',
            new_name='direccion',
        ),
        migrations.AlterField(
            model_name='persona',
            name='telefono',
            field=models.CharField(max_length=10),
        ),
    ]
