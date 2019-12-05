from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('ecoarauco',views.ecoarauco,name='ecoarauco'),
    path('EcoEncalada',views.EcoEncalada,name='EcoEncalada'),
    path('colife',views.colife,name='colife'),
    path('success',views.success,name='success'),
    path('error404',views.error404,name='error404'),
    path('departamentoinstance/<str:pk>', views.DepartamentoInstanceDetailView.as_view(), name='departamentoinstance_detail'),
    path('departamento/<str:pk>', views.DepartamentoDetailView.as_view(), name='departamento_detail'),
    path('cliente/<str:pk>', views.ClienteDetailView.as_view(), name='cliente_detail'),
    path('departamentosinstances/', views.DepartamentoInstanceListView.as_view(), name='departamentosinstances'),
    path('departamentos/', views.DepartamentoListView.as_view(), name='departamentos'),
    path('clientes/', views.ClienteListView.as_view(), name='clientes'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    #path(r'^departamentos/', views.DepartamentoListView.as_view(), name='departamentos'),
]

urlpatterns += [
    path('cliente/create/', views.ClienteCreate.as_view(), name='cliente_create'),
    path('cliente/<str:pk>/update/', views.ClienteUpdate.as_view(), name='cliente_update'),
    path('cliente/<str:pk>/delete/', views.ClienteDelete.as_view(), name='cliente_delete'),
    path('departamentoinstance/create/', views.DepartamentoInstanceCreate.as_view(), name='departamentoinstance_create'),
    path('departamentoinstance/<str:pk>/update/', views.DepartamentoInstanceUpdate.as_view(), name='departamentoinstance_update'),
    path('departamentoinstance/<str:pk>/delete/', views.DepartamentoInstanceDelete.as_view(), name='departamentoinstance_delete'),
    path('departamento/create/', views.DepartamentoCreate.as_view(), name='departamento_create'),
    path('departamento/<str:pk>/update/', views.DepartamentoUpdate.as_view(), name='departamento_update'),
    path('departamento/<str:pk>/delete/', views.DepartamentoDelete.as_view(), name='departamento_delete'),
]