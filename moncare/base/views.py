from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from login.models import Usuario
from base.forms import UsuarioForm
from base.models import Dispositivo_Medico

# Create your views here.
@login_required
def home(request):
    logged_in_user = request.user
    return render(request, 'base/home.html', {'user': logged_in_user})

@login_required
def logout(request):
    #logout(request) #Usuario logueado
    return redirect('login')

@login_required
def perfil(request):
    user_logged = request.user

    form = UsuarioForm(instance=user_logged)    
    return render(request, 'base/perfil.html', {'form': form, 'usuario': user_logged})

def get_dispositivos():
    #Retornara una lista con todos los dispositivos creados
    dispositivos = list(Dispositivo_Medico.objects.values_list('id', 'referencia', 'marca', 'asignado'))
    return dispositivos

def get_empleados():
    empleados = list(Usuario.objects.filter(tipo_usuario = 'Empleado de Salud').values_list('first_name','last_name', 'email'))
    #print("Aqui van los empleados:")
    #print(empleados)
    #return render(request, 'base/test_gestor_dispositivos.html', {'dispositivos':empleados})
    return empleados