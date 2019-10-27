from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('ecoarauco',views.ecoarauco,name='ecoarauco'),
    path('EcoEncalada',views.EcoEncalada,name='EcoEncalada'),
    path('colife',views.colife,name='colife'),
]