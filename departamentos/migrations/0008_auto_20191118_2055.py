# Generated by Django 2.2.6 on 2019-11-18 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamentos', '0007_auto_20191111_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamentoinstance',
            name='status',
            field=models.CharField(blank=True, choices=[('d', 'Disponible'), ('f', 'Fuera de servicio'), ('v', 'Vendido')], default='d', max_length=1),
        ),
    ]
