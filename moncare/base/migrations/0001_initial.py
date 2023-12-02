# Generated by Django 4.2.7 on 2023-12-02 05:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Historia_Clinica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('paciente', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Historia Clinica')),
            ],
        ),
        migrations.CreateModel(
            name='Dispositivo_Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_key', models.CharField(blank=True, max_length=40)),
                ('referencia', models.CharField(max_length=255, verbose_name='Referencia')),
                ('marca', models.CharField(max_length=50, verbose_name='Marca')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('asignado', models.BooleanField(default=False)),
                ('fecha_asignacion', models.DateTimeField(blank=True, null=True)),
                ('id_configurador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dispositivos_configurados', to=settings.AUTH_USER_MODEL)),
                ('id_creador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dispositivos_creados', to=settings.AUTH_USER_MODEL)),
                ('id_paciente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dispositivos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
