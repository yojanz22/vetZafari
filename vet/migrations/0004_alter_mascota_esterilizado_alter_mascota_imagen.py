# Generated by Django 4.0.4 on 2022-06-03 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vet', '0003_alter_mascota_sexo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='esterilizado',
            field=models.BooleanField(default=True, verbose_name='Esterilizado'),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='imagen',
            field=models.ImageField(null=True, upload_to='mascotas'),
        ),
    ]