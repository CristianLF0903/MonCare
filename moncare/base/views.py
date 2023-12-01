from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from login.models import Usuario
from base.forms import UsuarioForm

# Create your views here.
@login_required
def home(request):
    logged_in_user = request.user
    user = Usuario.objects.get(user = logged_in_user) #Usuario logueado
    return render(request, 'base/home.html', {'user': user})

@login_required
def logout(request):
    #logout(request) #Usuario logueado
    return redirect('login')

@login_required
def perfil(request):
    user_logged = request.user
    user = Usuario.objects.get(user = user_logged)

    form = UsuarioForm(instance=user.user)    
    return render(request, 'base/perfil.html', {'form': form, 'usuario': user})