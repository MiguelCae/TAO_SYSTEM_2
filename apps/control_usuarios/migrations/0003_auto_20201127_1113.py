# Generated by Django 3.1.2 on 2020-11-27 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control_usuarios', '0002_auto_20201122_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='edad',
            field=models.IntegerField(null=True),
        ),
    ]
