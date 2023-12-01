from django import forms
from login.models import Usuario
from django.contrib.auth.forms import UserChangeForm

class UsuarioForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ('username','first_name', 'last_name', 'email', 'password', 'tipo_usuario')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)