from django.contrib import admin

# Register your models here.

from . models import Cliente, Departamento, DepartamentoInstance

admin.site.register(Cliente)
admin.site.register(Departamento)
admin.site.register(DepartamentoInstance)
