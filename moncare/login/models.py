from django.db import models
from django.contrib.auth.models import User


class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    USER_TYPE_CHOICES = (
        ('Paciente', 'Paciente'),
        ('Familiar', 'Familiar'),
        ('Empleado de Salud', 'Empleado de Salud'),
    )

    Tipo_usuario = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name
