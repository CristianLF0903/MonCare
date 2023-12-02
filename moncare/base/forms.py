from django import forms
from django.contrib.auth.forms import UserChangeForm
from login.models import Usuario

# Formularios de Usuarios
class UsuarioForm(UserChangeForm):
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput,
        help_text="Deja este campo en blanco si no deseas cambiar la contraseña."
    )

    class Meta:
        model = Usuario
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'tipo_usuario')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Deshabilitar el campo username
        self.fields['username'].widget.attrs['readonly'] = True

        # Personalizar la etiqueta del campo password
        self.fields['password'].label = "Nueva Contraseña"

# Formularios de dispositivos