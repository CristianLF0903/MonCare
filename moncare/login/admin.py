from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class UsuarioAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'tipo_usuario')
    fieldsets = UserAdmin.fieldsets + (
        ('Información personalizada', {'fields': ('tipo_usuario',)}),
    )

admin.site.register(Usuario, UsuarioAdmin)
