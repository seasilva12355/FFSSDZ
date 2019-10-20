from django.db import models
from django.urls import reverse
import uuid

# Create your models here.

class Cliente(models.Model):
    rut_cliente = models.CharField(primary_key=True, max_length=13)
    id_departamento=models.ForeignKey('Departamento', on_delete=models.SET_NULL, null=True)
    primer_nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    correo = models.EmailField(max_length=200, help_text='Introduzca su correo electrónico')
    num_telefonico = models.CharField(max_length=9)

    class Meta:
        ordering = ['primer_nombre', 'apellido_paterno', 'apellido_materno']

    def get_absolute_url(self):
        return reverse('cliente-detail', args=[str(self.rut_cliente)])

    def __str__(self):
        return f'{self.primer_nombre}, {self.apellido_paterno}, {self.apellido_materno}'

class Departamento(models.Model):
    id_departamento=models.UUIDField(primary_key=True, default=uuid.uuid4)
    nombre=models.CharField(max_length=200)
    descripcion=models.TextField(max_length=1000, help_text='Ingresa la descripción del departamento')
    uf=models.IntegerField
    numero_habitaciones=models.IntegerField
    numero_banos=models.IntegerField

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        """Returns the url to access a detail record for this department."""
        return reverse('departamento-detail', args=[str(self.id_departamento)])
