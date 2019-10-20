from django.contrib import admin

# Register your models here.

from . models import Cliente, Departamento

admin.site.register(Cliente)
admin.site.register(Departamento)
