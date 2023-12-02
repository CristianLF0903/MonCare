from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render, redirect, get_object_or_404
from login.models import Usuario
from base.forms import UsuarioForm
from base.models import *

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

    if user_logged.tipo_usuario == 'Paciente' or user_logged.tipo_usuario == 'Familiar':

        if request.method == 'POST':
            form = UsuarioForm(request.POST, instance=user_logged)
            if form.is_valid():
                form.save()
                messages.success(request, 'Tu perfil ha sido actualizado correctamente.')
                return redirect('perfil')
            else:
                messages.error(request, 'Hubo un error al actualizar tu perfil. Por favor, verifica los datos ingresados.')
        else:
            form = UsuarioForm(instance=user_logged)

        return render(request, 'base/perfil.html', {'form': form, 'usuario': user_logged})

    elif user_logged == 'Administrador':

        if request.method == 'POST':
            form = UsuarioForm(request.POST, instance=user_logged)
            if form.is_valid():
                form.save()
                messages.success(request, 'Tu perfil ha sido actualizado correctamente.')
                return redirect('perfil')
            else:
                messages.error(request, 'Hubo un error al actualizar tu perfil. Por favor, verifica los datos ingresados.')
        else:
            form = UsuarioForm(instance=user_logged)

        return render(request, 'base/perfil.html', {'form': form, 'usuario': user_logged})

    else:
        if request.method == 'POST':
            form = UsuarioForm(request.POST, instance=user_logged)
            if form.is_valid():
                form.save()
                messages.success(request, 'Tu perfil ha sido actualizado correctamente.')
                return redirect('perfil')
            else:
                messages.error(request, 'Hubo un error al actualizar tu perfil. Por favor, verifica los datos ingresados.')
        else:
            form = UsuarioForm(instance=user_logged)

        return render(request, 'base/perfil.html', {'form': form, 'usuario': user_logged})

@login_required
def dispositivos(request):

    context = {
        'dispositivos': [],
    }

    return render(request, 'base/gestor-dispositivos.html', context)

@login_required
def editar_dispositivo(request, dispositivo_id):
    try:
        dispositivo = get_object_or_404(Dispositivo, id=dispositivo_id)
    except Dispositivo.DoesNotExist:
        messages.error(request, 'Hubo un error, no se encontró el dispositivo.')
        return redirect('dispositivos')  # Puedes redirigir a una página de error o renderizar una plantilla de error específica

    # Resto de la lógica de la vista para cuando el dispositivo existe
    # ...
    messages.succes(request, f'Dispositivo {dispositivo.refencia} ha sido editado correctamente.')
    return render(request, 'dispositivos.html', {'formulario': formulario, 'dispositivo': dispositivo})

@login_required
def eliminar_dispositivo(request, dispositivo_id):
    try:
        dispositivo = get_object_or_404(Dispositivo, id=dispositivo_id)
    except Dispositivo.DoesNotExist:
        messages.error(request, 'Hubo un error, no se encontró el dispositivo.')
        return redirect('dispositivos')  # Puedes redirigir a una página de error o renderizar una plantilla de error específica

    # Resto de la lógica de la vista para cuando el dispositivo existe
    # ...
    messages.succes(request, f'Dispositivo {dispositivo.refencia} eliminado correctamente.')
    return redirect('dispositivos')

@login_required
def agregar_dispositivo(request, dispositivo_id):
    # ...
    messages.succes(request, f'Dispositivo {dispositivo.refencia} eliminado correctamente.')
    return redirect('dispositivos')

