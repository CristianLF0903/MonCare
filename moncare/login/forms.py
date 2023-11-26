from django import forms
from django.contrib.auth.forms import AuthenticationForm
from login.models import Usuario


class LoginForm(forms.Form):
    Correo = forms.EmailField()
    Contraseña = forms.CharField(widget=forms.PasswordInput)


class RegistroForm(forms.ModelForm):

    USER_TYPE_CHOICES = (
        ('Paciente', 'Paciente'),
        ('Familiar', 'Familiar'),
        ('Empleado de Salud', 'Empleado de Salud'),
    )

    nombre = forms.CharField(label='Nombre', max_length=30, required=True)
    apellido = forms.CharField(label='Apellido', max_length=30, required=True)
    correo = forms.EmailField(label='Correo', max_length=254, required=True)
    contraseña = forms.CharField(
        label='Contraseña', widget=forms.PasswordInput, required=True)
    confirmar_contraseña = forms.CharField(
        label='Confirmar contraseña', widget=forms.PasswordInput, required=True)
    tipo_usuario = forms.ChoiceField(
        label='Tipo de usuario', choices=USER_TYPE_CHOICES)

    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'correo', 'contraseña',
                  'confirmar_contraseña', 'tipo_usuario']

    def clean(self):
        cleaned_data = super().clean()
        contraseña = cleaned_data.get("contraseña")
        confirmar_contraseña = cleaned_data.get("confirmar_contraseña")

        if contraseña != confirmar_contraseña:
            raise forms.ValidationError("Las contraseñas no coinciden.")

    def save(self, commit=True):
        user = super(RegistroForm, self).save(commit=False)
        user.nombre = self.cleaned_data['nombre']
        user.apellido = self.cleaned_data['apellido']
        user.correo = self.cleaned_data['correo']
        user.tipo_usuario = self.cleaned_data['tipo_usuario']

        if commit:
            user.save()

        return user
