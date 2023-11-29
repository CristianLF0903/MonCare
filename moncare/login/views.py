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
            usuario = Usuario.objects.create(
                user=user, Tipo_usuario=tipo_usuario)
            login(request, user)
            # Cambia 'index' por la URL a la que quieras redirigir después del registro
            return redirect('pagina_principal')
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
