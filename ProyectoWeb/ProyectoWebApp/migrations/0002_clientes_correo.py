# Generated by Django 4.1.7 on 2023-03-19 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoWebApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientes',
            name='correo',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
