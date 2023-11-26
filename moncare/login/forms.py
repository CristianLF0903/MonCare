from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Usuario
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    class Meta:
        model = Usuario
        fields = ('username', 'password')


class RegistroForm(UserCreationForm):
    Tipo_usuario = forms.ChoiceField(choices=Usuario.USER_TYPE_CHOICES)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegistroForm, self).__init__(*args, **kwargs)

        # Eliminar help_texts específicos si es necesario
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

    def save(self, commit=True):
        user = super().save(commit=False)
        tipo_usuario = self.cleaned_data['Tipo_usuario']

        if commit:
            user.save()
            usuario = Usuario.objects.create(
                user=user, Tipo_usuario=tipo_usuario)

        return user
