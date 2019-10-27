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

def contact(request):
    num_clientes= Cliente.objects.all().count()
    num_departamentos= Departamento.objects.all().count()
    
    return render(
        request,
        'contact.html',
        context={'num_departamentos':num_departamentos,'num_clientes':num_clientes},
    )

def about(request):
    num_clientes= Cliente.objects.all().count()
    num_departamentos= Departamento.objects.all().count()
    
    return render(
        request,
        'about.html',
        context={'num_departamentos':num_departamentos,'num_clientes':num_clientes},
    )

def ecoarauco(request):
    num_clientes= Cliente.objects.all().count()
    num_departamentos= Departamento.objects.all().count()
    
    return render(
        request,
        'ecoarauco.html',
        context={'num_departamentos':num_departamentos,'num_clientes':num_clientes},
    )

def EcoEncalada(request):
    num_clientes= Cliente.objects.all().count()
    num_departamentos= Departamento.objects.all().count()
    
    return render(
        request,
        'EcoEncalada.html',
        context={'num_departamentos':num_departamentos,'num_clientes':num_clientes},
    )

def colife(request):
    num_clientes= Cliente.objects.all().count()
    num_departamentos= Departamento.objects.all().count()
    
    return render(
        request,
        'colife.html',
        context={'num_departamentos':num_departamentos,'num_clientes':num_clientes},
    )