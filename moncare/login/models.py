from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    USER_TYPE_CHOICES = (
        ('Paciente', 'Paciente'),
        ('Familiar', 'Familiar'),
        ('Empleado de Salud', 'Empleado de Salud'),
    )

    Correo = models.EmailField(unique=True)
    Nombre = models.CharField(max_length=30)
    Apellido = models.CharField(max_length=30)
    Tipo_usuario = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)

    def __str__(self):
        return self.Nombre + " " + self.Apellido
