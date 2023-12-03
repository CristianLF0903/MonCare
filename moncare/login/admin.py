from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class UsuarioAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'tipo_usuario', 'is_admin', 
    'tipo_empleado','tiene_medico',)
    fieldsets = UserAdmin.fieldsets + (
        ('Información personalizada', {'fields': ('tipo_usuario', 'is_admin', 'tipo_empleado', 'tiene_medico',)}),
    )

admin.site.register(Usuario, UsuarioAdmin)
