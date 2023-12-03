from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    USER_TYPE_CHOICES = (
        ('Paciente', 'Paciente'),
        ('Familiar', 'Familiar'),
        ('Empleado de Salud', 'Empleado de Salud'),
    )

    EMPLOYE_TYPE_CHOICES = (
        ('Medico', 'Medico'),
        ('Cuidador', 'Cuidador'),
        ('Paramedico', 'Paramedico'),
        ('Empleado de Salud', 'Empleado de Salud'),
    )

    tipo_usuario = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    is_admin = models.BooleanField(default=False)
    tipo_empleado = models.CharField(max_length=20, choices=EMPLOYE_TYPE_CHOICES, null=True, blank=True)

    # Campo para almacenar pacientes (lista de usuarios)
    pacientes = models.ManyToManyField('self', symmetrical=False, related_name='mis_pacientes', blank=True)
    tiene_medico = models.BooleanField(default=False)
    # Campo para almacenar familiares (lista de usuarios)
    familiares = models.ManyToManyField('self', symmetrical=False, related_name='mis_familiares', blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    