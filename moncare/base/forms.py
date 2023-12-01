from django import forms
from login.models import Usuario
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class UsuarioForm(UserChangeForm):
    #useruario = Usuario.objects.get(user = user_logged)
    Tipo_usuario = forms.ChoiceField(choices=Usuario.USER_TYPE_CHOICES)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Configuración de widgets y atributos
        self.fields['Tipo_usuario'].required = True
        self.fields['Tipo_usuario'].widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super().clean()

        # Habilitar el botón de guardar solo si hay cambios en los campos
        if not self.has_changed():
            raise forms.ValidationError("No se realizaron cambios.")

        return cleaned_data