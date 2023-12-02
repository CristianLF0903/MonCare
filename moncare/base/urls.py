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

    # Dispositivos
    path("Moncare/empleados", empleados, name="empleados"),
    path('Moncare/eliminar_empleado/<int:empleado_id>/', eliminar_empleado, name='elimiar_empleado'),
    path('Moncare/editar_empleado/<int:empleado_id>/', editar_empleado, name='editar_empleado'),

]
