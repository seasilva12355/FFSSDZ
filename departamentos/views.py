from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cliente, Departamento, DepartamentoInstance
from django.views import generic

# Create your views here.
class ClienteListView(generic.ListView):
    model = Cliente
    paginate_by = 10

class ClienteCreate(CreateView):
    model = Cliente
    fields = '__all__'

class ClienteUpdate(UpdateView):
    model = Cliente
    fields = ['nombre_completo','correo','num_telefonico']

class ClienteDelete(DeleteView):
    model = Cliente
    success_url = reverse_lazy('clientes')

class ClienteDetailView(generic.DetailView):
    model= Cliente

class DepartamentoListView(generic.ListView):
    model = Departamento
    paginate_by = 10

class DepartamentoCreate(CreateView):
    model = Departamento
    fields = '__all__'

class DepartamentoUpdate(UpdateView):
    model = Departamento
    fields = ['nombre','descripcion','uf','numero_habitaciones','numero_banos']

class DepartamentoDelete(DeleteView):
    model = Departamento
    success_url = reverse_lazy('departamentos')

class DepartamentoDetailView(generic.DetailView):
    model= Departamento

class DepartamentoInstanceCreate(CreateView):
    model = DepartamentoInstance
    fields = '__all__'

class DepartamentoInstanceUpdate(UpdateView):
    model = DepartamentoInstance
    fields = ['status']

class DepartamentoInstanceDelete(DeleteView):
    model = DepartamentoInstance
    success_url = reverse_lazy('departamentosinstances')

class DepartamentoInstanceDetailView(generic.DetailView):
    model= DepartamentoInstance

class DepartamentoInstanceListView(generic.ListView):
    model = DepartamentoInstance
    paginate_by = 10



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

def success(request):
    num_clientes= Cliente.objects.all().count()
    num_departamentos= Departamento.objects.all().count()
    
    return render(
        request,
        'success.html',
        context={'num_departamentos':num_departamentos,'num_clientes':num_clientes},
    )

def error404(request):
    return render(
        request,
        'error404.html',
    )

def cliente_detail_view(request,pk):
    try:
        rut_cliente=Cliente.objects.get(pk=pk)
    except Cliente.DoesNotExist:
        raise Http404("Cliente no existe.")

    #rut_cliente=get_object_or_404(Cliente, pk=pk)
    
    return render(
        request,
        'departamentos/cliente_detail.html',
        context={'cliente':rut_cliente,}
    )

def departamento_detail_view(request,pk):
    try:
        id_departamento=Departamento.objects.get(pk=pk)
    except Departamento.DoesNotExist:
        return render(
            request,
            'error404.html',
        )

    #id_departamento=get_object_or_404(Departamento, pk=pk)
    
    return render(
        request,
        'departamentos/departamento_detail.html',
        context={'departamento':id_departamento,}
    )

def departamentoinstance_detail_view(request,pk):
    try:
        id=DepartamentoInstance.objects.get(pk=pk)
    except DepartamentoInstance.DoesNotExist:
        return render(
            request,
            'error404.html',
        )

    #id_departamento=get_object_or_404(Departamento, pk=pk)
    
    return render(
        request,
        'departamentos/departamentoinstance_detail.html',
        context={'departamentoinstance':id,}
    )