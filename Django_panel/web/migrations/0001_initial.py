# Generated by Django 3.2 on 2023-05-07 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TblAlumno',
            fields=[
                ('alumno_id', models.AutoField(primary_key=True, serialize=False)),
                ('alumno_nombre', models.CharField(max_length=100)),
                ('alumno_email', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'tbl_alumno',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblMatricula',
            fields=[
                ('matricula_id', models.AutoField(primary_key=True, serialize=False)),
                ('matricula_grupo', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'tbl_matricula',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblProfesor',
            fields=[
                ('profesor_id', models.AutoField(primary_key=True, serialize=False)),
                ('profesor_nombre', models.CharField(max_length=255)),
                ('profesor_email', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'tbl_profesor',
                'managed': False,
            },
        ),
    ]
