from django.contrib import admin
from django.urls import path
from base.views import *

urlpatterns = [
    path('Moncare/', home, name='pagina_principal'),
    path('Moncare/logout/', logout, name='logout'),
    path('Moncare/perfil/', perfil, name='perfil'),

    # Dispositivos
    path("Moncare/dispositivos", dispositivos, name="dispositivos"),
    path('Moncare/eliminar_dispositivo/<int:dispositivo_id>/', eliminar_dispositivo, name='elimiar_dispositivo'),
    path('Moncare/editar_dispositivo/<int:dispositivo_id>/', editar_dispositivo, name='editar_dispositivo'),
    path('Moncare/agregar_dispositivo/', agregar_dispositivo, name='agregar_dispositivo'),

]
