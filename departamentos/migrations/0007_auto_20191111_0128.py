# Generated by Django 2.2.6 on 2019-11-11 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamentos', '0006_departamentoinstance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamentoinstance',
            name='id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]