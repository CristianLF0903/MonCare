from django.contrib import admin
from .models import (
    Dispositivo_Medico,
    Nivel_Visualizacion,
    Historia_Clinica,
    Medicion,
    Rango,
    Episodio_Medico,
    Episodio_Revisa_Medicion,
    Registro,
    Notificacion,
    Alarma,
    Nivel_Autorizacion
)

# Aquí registras cada modelo para que aparezca en el admin
admin.site.register(Dispositivo_Medico)
admin.site.register(Nivel_Visualizacion)
admin.site.register(Historia_Clinica)
admin.site.register(Medicion)
admin.site.register(Rango)
admin.site.register(Episodio_Medico)
admin.site.register(Episodio_Revisa_Medicion)
admin.site.register(Registro)
admin.site.register(Notificacion)
admin.site.register(Alarma)
admin.site.register(Nivel_Autorizacion)
