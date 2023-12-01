from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from login.forms import RegistroForm, LoginForm
from login.models import Usuario


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
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
            return redirect('pagina_principal')
    else:
        form = LoginForm()
    return render(request, 'login/login.html', {'form': form})
