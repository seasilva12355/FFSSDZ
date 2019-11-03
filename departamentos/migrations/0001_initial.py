# Generated by Django 2.2.6 on 2019-11-02 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id_departamento', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField(max_length=1000)),
                ('uf', models.IntegerField(default=0)),
                ('numero_habitaciones', models.IntegerField(default=0)),
                ('numero_banos', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('rut_cliente', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('nombre_completo', models.CharField(max_length=300)),
                ('correo', models.EmailField(max_length=200)),
                ('num_telefonico', models.CharField(max_length=9)),
                ('id_departamento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='departamentos.Departamento')),
            ],
        ),
    ]
