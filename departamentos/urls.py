from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('ecoarauco',views.ecoarauco,name='ecoarauco'),
    path('EcoEncalada',views.EcoEncalada,name='EcoEncalada'),
    path('colife',views.colife,name='colife'),
    path('departamento/<int:pk>', views.DepartamentoDetailView.as_view(), name='departamento_detail'),
    path('cliente/<int:pk>', views.ClienteDetailView.as_view(), name='cliente_detail'),
    path('departamentos/', views.DepartamentoListView.as_view(), name='departamentos'),
    path('clientes/', views.ClienteListView.as_view(), name='clientes'),
    #path(r'^departamentos/', views.DepartamentoListView.as_view(), name='departamentos'),
    
]

urlpatterns += [
    path('cliente/create/', views.ClienteCreate.as_view(), name='cliente_create'),
    path('cliente/<int:pk>/update/', views.ClienteUpdate.as_view(), name='cliente_update'),
    path('cliente/<int:pk>/delete/', views.ClienteDelete.as_view(), name='cliente_delete'),
    path('departamento/create/', views.DepartamentoCreate.as_view(), name='departamento_create'),
    path('departamento/<int:pk>/update/', views.DepartamentoUpdate.as_view(), name='departamento_update'),
    path('departamento/<int:pk>/delete/', views.DepartamentoDelete.as_view(), name='departamento_delete'),
]