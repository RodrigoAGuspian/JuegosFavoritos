# Generated by Django 2.0.2 on 2018-03-09 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listavj', '0005_videojuego_plataforma'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desarrollador',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='logo'),
        ),
        migrations.AlterField(
            model_name='distribuidor',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='logo'),
        ),
    ]
