# Generated by Django 3.1.2 on 2020-11-23 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control_usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rol',
            name='rol',
            field=models.CharField(choices=[('Colaborador', 'Colaborador'), ('Adoptante', 'Adoptante'), ('Veterinario', 'Veterinario'), ('Director', 'Director')], max_length=20),
        ),
    ]
