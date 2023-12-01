from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from login.forms import RegistroForm, LoginForm
from login.models import Usuario


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            tipo_usuario = form.cleaned_data['Tipo_usuario']
            # Verificar si ya existe un objeto Usuario para este usuario
            usuario, created = Usuario.objects.get_or_create(user=user)

            if created:
                # Solo si se creó un nuevo objeto Usuario, configurar el tipo de usuario
                tipo_usuario = form.cleaned_data['Tipo_usuario']
                usuario.Tipo_usuario = tipo_usuario
                usuario.save()

            login(request, user)
            return redirect('perfil')
    else:
        form = RegistroForm()
    return render(request, 'login/registro.html', {'form': form})


def iniciar_sesion(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Cambia 'index' por la URL a la que quieras redirigir después del inicio de sesión
            return redirect('pagina_principal')
    else:
        form = LoginForm()
    return render(request, 'login/login.html', {'form': form})
