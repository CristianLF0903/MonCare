from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.utils.crypto import get_random_string
from login.models import Usuario
# Create your models here.

class Dispositivo_Medico(models.Model):
    #Esta pensado para usar un generador de api_key
    api_key = models.CharField(max_length=40, blank=True, null=False)
    referencia = models.CharField(max_length=255,verbose_name="Referencia" )
    marca = models.CharField(max_length=50, verbose_name="Marca")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    asignado = models.BooleanField(default=False)
    fecha_asignacion = models.DateTimeField(null=True, blank=True)
    id_creador = models.ForeignKey(Usuario, on_delete=models.SET_NULL, related_name="dispositivos_creados", null=True, blank=True)
    id_paciente = models.ForeignKey(Usuario, on_delete=models.SET_NULL, related_name="dispositivos", null=True, blank=True)
    id_configurador = models.ForeignKey(Usuario, on_delete=models.SET_NULL, related_name="dispositivos_configurados", null=True, blank=True)

@receiver(pre_save, sender=Dispositivo_Medico)
def generar_api_key(sender, instance, **kwargs):
    # Generar una API key
    instance.api_key = get_random_string(length=40)

class Historia_Clinica(models.Model):
    fecha_nacimiento = models.DateField(verbose_name="Fecha de Nacimiento")
    paciente = models.OneToOneField(Usuario, on_delete=models.CASCADE, verbose_name='Historia Clinica')