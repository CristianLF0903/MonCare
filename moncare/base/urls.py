from django.contrib import admin
from django.urls import path
from base.views import home, logout, perfil

urlpatterns = [
    path('Moncare/', home, name='pagina_principal'),
    path('Moncare/logout/', logout, name='logout'),
    path('Moncare/perfil/', perfil, name='perfil'),

]
