# Generated by Django 2.1.2 on 2018-10-16 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='correo',
            field=models.EmailField(max_length=50),
        ),
    ]
