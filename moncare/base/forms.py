from django import forms
from django.contrib.auth.forms import UserChangeForm
from login.models import Usuario
from base.models import Dispositivo_Medico

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
class DispositivoMedicoForm(forms.ModelForm):
    class Meta:
        model = Dispositivo_Medico
        fields = ('referencia', 'marca')


class DispositivoMedicoForm_edit(forms.ModelForm):
    class Meta:
        model = Dispositivo_Medico
        fields = ['referencia', 'marca', 'asignado', 'id_paciente', 'id_configurador']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Puedes personalizar los widgets, agregar clases CSS, etc.
        self.fields['asignado'].widget.attrs['class'] = 'form-check-input'  # Ejemplo: agregar una clase Bootstrap a un campo booleano

        # Filtrar opciones de usuario según el tipo de usuario
        self.fields['id_paciente'].queryset = Usuario.objects.filter(tipo_usuario='Paciente')
        self.fields['id_configurador'].queryset = Usuario.objects.filter(tipo_usuario='Empleado de Salud')

        # Actualizar los valores iniciales de los campos
        instance = kwargs.get('instance')
        if instance:
            self.fields['referencia'].initial = instance.referencia
            self.fields['marca'].initial = instance.marca
            self.fields['asignado'].initial = instance.asignado
            self.fields['id_paciente'].initial = instance.id_paciente
            self.fields['id_configurador'].initial = instance.id_configurador