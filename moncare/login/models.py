from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    USER_TYPE_CHOICES = (
        ('Paciente', 'Paciente'),
        ('Familiar', 'Familiar'),
        ('Empleado de Salud', 'Empleado de Salud'),
    )

    tipo_usuario = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    