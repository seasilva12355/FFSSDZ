from departamentos.models import Departamento,Cliente
from django.test import TestCase

# Create your tests here.
class TestCliente(TestCase):

    def clienteCrearTrue(self):
        Cliente.objects.Create(rut_cliente='12.345.678-k')
        Cliente.objects.ForeignKey(id_departamento='2')
        Cliente.objects.Create(nombre_completo='Armando Bronca Segura')
        Cliente.objects.Create(correo='elcorreo@correo.com')
        Cliente.objects.Create(num_telefonico= 911223344)
        self.assertTrue(False)

    def clienteCrearFalse(self):
        Cliente.objects.Create(rut_cliente='dddddd')
        Cliente.objects.ForeignKey(id_departamento='2')
        Cliente.objects.Create(nombre_completo='Armando Bronca Segura')
        Cliente.objects.Create(correo='elcorreo@correo.com')
        Cliente.objects.Create(num_telefonico= 'aaaaa')
        self.assertFalse(False)


    def clienteEliminarTrue(self):
        Cliente.objects.Create(rut_cliente='12.345.678-k')
        Cliente.objects.ForeignKey(id_departamento='2')
        Cliente.objects.Create(nombre_completo='Armando Bronca Segura')
        Cliente.objects.Create(correo='elcorreo@correo.com')
        Cliente.objects.Create(num_telefonico= 911223344)

        Cliente.Create()
        self = Cliente.on_delete()
        self.assertEquals(True)

    def clienteEliminarFalse(self):
        Cliente.objects.Create(rut_cliente='dddddd')
        Cliente.objects.ForeignKey(id_departamento='2')
        Cliente.objects.Create(nombre_completo='Armando Bronca Segura')
        Cliente.objects.Create(correo='elcorreo@correo.com')
        Cliente.objects.Create(num_telefonico= 'aaaaa')

        self = Cliente.on_delete()
        self.assertEquals(False)

    def Cliente_Rut_Max_Length(self):
        max_length = Cliente._meta.get_field('rut_cliente').max_length
        self.assertEquals(max_length,13)

    def Cliente_Nombre_Max_Length(self):
        max_length = Cliente._meta.get_field('nombre_completo').max_length
        self.assertEquals(max_length,300)

    def Cliente_Correo_Max_Length(self):
        max_length = Cliente._meta.get_field('correo').max_length
        self.assertEquals(max_length,200)

    def Cliente_NumeroT_Max_Length(self):
        max_length = Cliente._meta.get_field('num_telefonico').max_length
        self.assertEquals(max_length,9)


    def ClienteTestLabel(self):
        field_label = cliente._meta.get_field('nombre_completo').verbose_name
        self.assertEquals(field_label,'nombre_completo')



class TestDepartamento(TestCase):

    def DepartamentoCrearTrue(self):
        Departamento.objects.create(id_departamento='1')
        Departamento.objects.create(nombre='EcoArauco')
        Departamento.objects.create(descripcion='Descripicion departamento')
        Departamento.objects.create(uf='245')
        Departamento.objects.create(numero_habitaciones= 2)
        Departamento.objects.create(numero_banos= 1)
        self.assertTrue(False)

    def DepartamentoCrearFalse(self):
        Departamento.objects.create(id_departamento='1')
        Departamento.objects.create(nombre='grancasa')
        Departamento.objects.create(descripcion='Descripicion departamento')
        Departamento.objects.create(uf='kkk')
        Departamento.objects.create(numero_habitaciones= dos)
        Departamento.objects.create(numero_banos= tres)
        self.assertFalse(False)

    def DepartamentoEliminarTrue(self):
        Departamento.objects.create(id_departamento='1')
        Departamento.objects.create(nombre='EcoArauco')
        Departamento.objects.create(descripcion='Descripicion departamento')
        Departamento.objects.create(uf='245')
        Departamento.objects.create(numero_habitaciones= 2)
        Departamento.objects.create(numero_banos= 1)

        Departamento.Create()
        self = Departamento.on_delete()
        self.assertEquals(True)

    def DepartamentoEliminarTrue(self):
        Departamento.objects.create(id_departamento='1')
        Departamento.objects.create(nombre='EcoArauco')
        Departamento.objects.create(descripcion='Descripicion departamento')
        Departamento.objects.create(uf='245')
        Departamento.objects.create(numero_habitaciones= 2)
        Departamento.objects.create(numero_banos= 1)

        self = Departamento.on_delete()
        self.assertEquals(False)

    def Departamento_Nombre_Max_length(self):
        max_length = Departamento._meta.get_field('nombre').max_length
        self.assertEquals(max_length,200)

    def Departamento_Descripcion_Max_length(self):
        max_length = Departamento._meta.get_field('descripcion').max_length
        self.assertEquals(max_length,1000)

    def DepartamentoTestLabel(self):
        field_label = Departamento._meta.get_field('nombre').verbose_name
        self.assertEquals(field_label,'nombre')
