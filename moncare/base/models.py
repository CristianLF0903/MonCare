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

class Nivel_Visualizacion(models.Model):
    NIVEL_ACCESO_CHOICES = [
        ('acesso completo','Acceso Completo'),
        ('acceso parcial', 'Acceso Parcial'),
        ('acceso por rol', 'Acceso por Rol'),
        ('acceso solo lectura', 'Acceso Solo Lectura'),
        ('acceso de emergencia', 'Acceso de Emergencia'),
        ('sin acceso', 'Sin Acceso')
    ]
    permisos = models.CharField(max_length=255, verbose_name='Permisos')
    temporal = models.BooleanField(default=False, verbose_name='Temporal')
    tipo_acceso = models.CharField(max_length=50,
        choices=NIVEL_ACCESO_CHOICES,
        default='sin acceso', 
        verbose_name='Tipos de Acceso'
    )
    
class Historia_Clinica(models.Model):
    fecha_nacimiento = models.DateField(null=True, blank =True, verbose_name="Fecha de Nacimiento")
    num_seguro = models.IntegerField(null=True, blank =True, verbose_name='Numero de Seguro')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    paciente = models.OneToOneField(Usuario, on_delete=models.CASCADE, verbose_name='Historia Clinica')
    nivel_visualizacion = models.ForeignKey(Nivel_Visualizacion, on_delete=models.SET_NULL, related_name="nivel_visualizacion", null=True, blank=True )

class Medicion(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    parametro = models.CharField(max_length=255, null=False, blank =True, verbose_name='Parametro medido')
    valor = models.FloatField(null=False, blank=False, verbose_name='Valor de la Medicion')
    unidades = models.CharField(max_length=20, null=False, blank=True, verbose_name='Unidades de la Medicion')
    id_dispositivo = models.ForeignKey(Dispositivo_Medico, on_delete=models.SET_NULL, related_name="Dipositivo_medidor", null=True, blank=True)
    
class Rango(models.Model):
    parametro = models.CharField(max_length=255, null=False, blank =True, verbose_name='Parametro a verificar')
    valor_min = models.FloatField(null=True, blank=True, verbose_name='Valor minimo')
    valor_max = models.FloatField(null=True, blank=True, verbose_name='Valor maximo')
    unidades = models.CharField(max_length=20, null=False, blank=True, verbose_name='Unidades de la Medicion')

class Episodio_Medico(models.Model):
    NIVEL_RIESGO_CHOICES = [
        ('moderado', 'Moderado'),
        ('critico', 'Critico')
    ]
    nivel_riesgo = models.CharField(
        max_length=10,
        choices=NIVEL_RIESGO_CHOICES,
        default='moderado',
        verbose_name='Nivel de Acceso'
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    id_creador = models.ForeignKey(Usuario, on_delete=models.SET_NULL, related_name="Episodios_creados", null=True, blank=True)
    id_paciente = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="Episodios_propios_paciente", null=True, blank=True)
    id_rango = models.OneToOneField(Rango, on_delete=models.CASCADE, related_name='Rango_medidas', null=False, blank=True)

#Este modelo es creado como intermediario entre Episodio Medico y Medicion con relacion muchos a muchos
class Episodio_Revisa_Medicion(models.Model):
    fecha_revision = models.DateTimeField(auto_now_add=True)
    episodio_medico = models.ForeignKey(Episodio_Medico, on_delete=models.CASCADE, related_name='Reviso_medicion', null=False, blank=False)
    medicion = models.ForeignKey(Medicion, on_delete=models.CASCADE, related_name='Medicion_revisada', null=False, blank=False)
    #Estos campos pertenecian a Medicion, pero se trasladan a este modelo para que tenga mas sentido
    revisada_por_alarma = models.BooleanField(default=False, null=False, blank=True)
    revisada_por_notificacion = models.BooleanField(default=False, null=False, blank=True)

class Registro(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Registro')
    descripcion = models.CharField(max_length=255, verbose_name='Descripcion del Registro', null=False)
    id_historia_clinica = models.ForeignKey(Historia_Clinica, on_delete=models.CASCADE, null=False, blank=False)
    id_medicion = models.OneToOneField(Medicion, on_delete=models.CASCADE, related_name='Registro_medidas', null=False, blank=True)

class Notificacion(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de notificacion')
    id_paciente = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='Paciente_notificacion', null=False, blank=True)
    mensaje = models.CharField(max_length=255, null=False, blank=True, verbose_name="Mensaje")
    leido = models.BooleanField(default=False, verbose_name='Fue leido?')
    id_receptor = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=False, blank=False,verbose_name='Receptor de Notificacion')
    id_episodio_medico = models.ForeignKey(Episodio_Medico, on_delete=models.CASCADE, null=False, blank=True, verbose_name='Episodio Medico disparador')
    
class Alarma(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de alarma')
    id_paciente = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='Paciente_alarma', null=False, blank=True)
    mensaje = models.CharField(max_length=255, null=False, blank=True, verbose_name="Mensaje")
    leido = models.BooleanField(default=False, verbose_name='Fue leido?')
    id_paramedico = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=False, blank=False,verbose_name='Paramedico asignado')
    id_episodio_medico = models.ForeignKey(Episodio_Medico, on_delete=models.CASCADE, null=False, blank=True, verbose_name='Episodio Medico disparador')

class Nivel_Autorizacion(models.Model):
    PERMISOS_CHOICES = [
        ('sin autorizacion', 'Sin Autorizacion'),
        ('visualizar historia clinica', 'Visualizar Historia Clinica'),
        ('visualizar notificaciones', 'Nisualizar Notificaciones'),
        ('visualizar alarmas', 'Visualizar Alarmas'),
        ('visualizar empleados','Visualizar Empleados'),
        ('editar empleados','Editar Empleados'),
        ('eliminar empleados', 'Eliminar Empleados'),
        ('crear empleados', 'Crear Empleados'),
        ('contratar empleados', 'Contratar Empleados'),
        ('despedir empleados', 'Despedir Empleados'),
        ('crear dispositivos', 'Crear Dispositivos'),
        ('configurar dispositivos', 'Configurar Dispositivos'),
        ('asignar cuidador', 'Asignar Cuidador'),
        ('reemplazar cuidador', 'Reempleazar Cuidador'),
        ('definir episodios medicos', 'Definir Episodios Medicos'),
        ('habilitar familiar', 'Habilitar Familiar')
    ]
    roles=models.CharField(max_length=100, null=False, blank=True, verbose_name='Rol')
    permisos = models.CharField(
            max_length=255,
            choices=PERMISOS_CHOICES,
            default='sin autorizacion',
            verbose_name='Permisos permitidos'
    )