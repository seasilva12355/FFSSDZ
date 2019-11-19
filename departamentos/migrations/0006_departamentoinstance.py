# Generated by Django 2.2.6 on 2019-11-11 03:52

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('departamentos', '0005_auto_20191104_0116'),
    ]

    operations = [
        migrations.CreateModel(
            name='DepartamentoInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('fecha_instancia', models.DateField()),
                ('status', models.CharField(blank=True, choices=[('d', 'Disponible'), ('f', 'Fuera de servicio'), ('v', 'Vendido')], default='d', help_text='Disponibilidad de departamento', max_length=1)),
                ('departamento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='departamentos.Departamento')),
            ],
        ),
    ]
