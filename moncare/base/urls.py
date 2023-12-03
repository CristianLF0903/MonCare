from django.contrib import admin
from django.urls import path
from base.views import *

urlpatterns = [
    path('Moncare/', home, name='pagina_principal'),
    path('logout/', logout_view, name='logout'),
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

    # Pacientes
    path("Moncare/pacientes/", pacientes, name="pacientes"),
    path('Moncare/agregar_paciente/', agregar_paciente1, name='agregar_paciente1'),
    path('Moncare/agregar_paciente/<int:paciente_id>/', agregar_paciente, name='agregar_paciente'),
    path('Moncare/eliminar_paciente/<int:paciente_id>/', eliminar_paciente, name='elimiar_paciente'),
    path('Moncare/detalles_paciente/<int:paciente_id>/', detalles_paciente, name='detalles_paciente'),
    path('Moncare/agregar_dispositivo_paciente/<int:paciente_id>/<int:dispositivo_id>/', agregar_dispositivo_paciente, name='agregar_dispositivo_paciente'),
    path("Moncare/agregar_dispositivo/<int:paciente_id>", agregar_dispositivo_p, name="agregar_dispositivo_p"),
    path("Moncare/eliminar_dispositivo/<int:dispositivo_id>", eliminar_dispositivo_p, name="eliminar_dispositivo_p"),
    path("Moncare/asignar_cuidador/<int:paciente_id>", agregar_cuidador_p, name="asignar_cuidador_list"),
    path("Moncare/asignar_cuidador/<int:paciente_id>/<int:cuidador_id>", agregar_cuidador_paciente, name="asignar_cuidador"),
    path("Moncare/eliminar_cuidador/<int:paciente_id>/<int:cuidador_id>", eliminar_cuidador_p, name="eliminar_cuidador"),

]
