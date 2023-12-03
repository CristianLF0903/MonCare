# Generated by Django 4.2.7 on 2023-12-02 21:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_alter_usuario_tipo_empleado'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='familiares',
            field=models.ManyToManyField(blank=True, related_name='mis_familiares', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='usuario',
            name='pacientes',
            field=models.ManyToManyField(blank=True, related_name='mis_pacientes', to=settings.AUTH_USER_MODEL),
        ),
    ]
