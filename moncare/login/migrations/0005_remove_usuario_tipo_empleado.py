# Generated by Django 4.2.7 on 2023-12-02 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_alter_usuario_tipo_empleado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='tipo_empleado',
        ),
    ]
