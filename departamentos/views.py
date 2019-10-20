from django.shortcuts import render
from .models import Cliente, Departamento

# Create your views here.

def index(request):
    num_clientes= Cliente.objects.all().count()
    num_departamentos= Departamento.objects.all().count()
    
    return render(
        request,
        'index.html',
        context={'num_departamentos':num_departamentos,'num_clientes':num_clientes},
    )