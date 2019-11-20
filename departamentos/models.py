from django.db import models
from django.urls import reverse
import uuid

# Create your models here.

class Cliente(models.Model):
    rut_cliente = models.CharField(primary_key=True, max_length=13)
    id_departamento=models.ForeignKey('Departamento', on_delete=models.SET_NULL, null=True)
    nombre_completo = models.CharField(max_length=300)
    correo = models.EmailField(max_length=200)
    num_telefonico = models.CharField(max_length=9)

    def get_absolute_url(self):
        return reverse('cliente_detail', args=[str(self.rut_cliente)])

    def __str__(self):
        return self.rut_cliente

class Departamento(models.Model):
    id_departamento=models.CharField(primary_key=True, max_length=10)
    nombre=models.CharField(max_length=200)
    descripcion=models.TextField(max_length=1000)
    uf=models.IntegerField(default=0)
    numero_habitaciones=models.IntegerField(default=0)
    numero_banos=models.IntegerField(default=0)

    def __str__(self):
        return self.id_departamento

    def get_absolute_url(self):
        """Returns the url to access a detail record for this department."""
        return reverse('departamento_detail', args=[str(self.id_departamento)])

class DepartamentoInstance(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    departamento = models.ForeignKey('Departamento', on_delete=models.SET_NULL, null=True)
    fecha_instancia = models.DateField()

    LOAN_STATUS = (
        ('d', 'Disponible'),
        ('f', 'Fuera de servicio'),
        ('v', 'Vendido'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='d',
    )

    def __str__(self):
        """String for representing the Model object."""
        return self.id

    def get_absolute_url(self):
        """Returns the url to access a detail record for this department."""
        return reverse('departamentoinstance_detail', args=[str(self.id)])