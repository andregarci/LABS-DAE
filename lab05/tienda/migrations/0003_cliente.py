# Generated by Django 4.2 on 2023-04-20 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('dni', models.CharField(max_length=8)),
                ('telefono', models.CharField(max_length=15)),
                ('direccion', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('fecha_nacimiento', models.DateField()),
                ('fecha_publicacion', models.DateTimeField(default='date published')),
            ],
        ),
    ]
