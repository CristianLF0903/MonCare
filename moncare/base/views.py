from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from login.models import Usuario
from base.forms import *
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

    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=user_logged)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu perfil ha sido actualizado correctamente.')
            return redirect(request, 'perfil')
        else:
            messages.error(request, 'Hubo un error al actualizar tu perfil. Por favor, verifica los datos ingresados.')
            return redirect(request, 'perfil')
    else:
        form = UsuarioForm(instance=user_logged)

    return render(request, 'base/perfil.html', {'form': form, 'usuario': user_logged})

# Dispositivo medico
@login_required
def dispositivos(request):
    user_logged = request.user

    if user_logged.is_admin:

        dispositivos = list(Dispositivo_Medico.objects.values_list('id', 'referencia', 'marca', 'asignado'))
        context = {
            'dispositivos': dispositivos,
        }

        return render(request, 'base/gestor-dispositivos.html', context)

    else:
        messages.error(request, 'No tienes acceso a esta vista')
        return redirect('pagina_principal')

@login_required
def editar_dispositivo(request, dispositivo_id):
    try:
        dispositivo = get_object_or_404(Dispositivo_Medico, id=dispositivo_id)
    except dispositivo.DoesNotExist:
        messages.error(request, 'Hubo un error, no se encontró el dispositivo.')
        return redirect('dispositivos')  # Puedes redirigir a una página de error o renderizar una plantilla de error específica

    if request.method == 'POST':
        form = DispositivoMedicoForm_edit(request.POST, instance=dispositivo)
        if form.is_valid():
            form.save()
            messages.success(request, f'Dispositivo {dispositivo.referencia} ha sido actualizado correctamente.')
            return redirect('dispositivos')
        else:
            messages.error(request, 'Hubo un error al actualizar el dispositivo. Por favor, verifica los datos ingresados.')
    else:
        form = DispositivoMedicoForm_edit(instance=dispositivo)

    return render(request, 'base/formulario.html', {'form': form, 'accion': 'Editar', 'entidad': f'dispositivo {dispositivo.id}'})

@login_required
def eliminar_dispositivo(request, dispositivo_id):
    try:
        dispositivo = get_object_or_404(Dispositivo_Medico, id=dispositivo_id)
    except dispositivo.DoesNotExist:
        messages.error(request, 'Hubo un error, no se encontró el dispositivo.')
        return redirect('dispositivos')  # Puedes redirigir a una página de error o renderizar una plantilla de error específica

    dispositivo.delete()
    messages.success(request, f'Dispositivo {dispositivo.referencia} eliminado correctamente.')
    return redirect('dispositivos')

@login_required
def agregar_dispositivo(request):

    if request.method == 'POST':
        form = DispositivoMedicoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dispositivo agregado correctamente.')
            return redirect('dispositivos')
        else:
            messages.error(request, 'Hubo un error al crear el dispositivo. Por favor, verifica los datos ingresados.')
    else:
        form = DispositivoMedicoForm()

    return render(request, 'base/formulario.html', {'form': form, 'accion': 'Nuevo', 'entidad': 'dispositivo'})

# Empleados
@login_required
def empleados(request):
    user_logged = request.user

    if user_logged.is_admin:
        empleados = list(Usuario.objects.filter(tipo_usuario = 'Empleado de Salud', is_admin=False).values_list('id','first_name','last_name', 'email', 'tipo_empleado'))

        return render(request, 'base/gestor-empleados.html', {'empleados': empleados})

    else:
        messages.error(request, 'No tienes acceso a esta vista')
        return redirect('pagina_principal')

@login_required
def editar_empleado(request, empleado_id):
    try:
        empleado = get_object_or_404(Usuario, id=empleado_id)
    except empleado.DoesNotExist:
        messages.error(request, 'Hubo un error, no se encontró el usuario.')
        return redirect('empleados')  # Puedes redirigir a una página de error o renderizar una plantilla de error específica

    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            messages.success(request, f'Empleado {empleado} ha sido actualizado correctamente.')
            return redirect('empleados')
        else:
            messages.error(request, 'Hubo un error al actualizar el dispositivo. Por favor, verifica los datos ingresados.')
    else:
        form = EmpleadoForm(instance=empleado)

    return render(request, 'base/formulario.html', {'form': form, 'accion': 'Editar', 'entidad': f'Empleado {empleado}'})

@login_required
def eliminar_empleado(request, empleado_id):
    try:
        empleado = get_object_or_404(Usuario, id=empleado_id)
    except empleado.DoesNotExist:
        messages.error(request, 'Hubo un error, no se encontró el usaurio.')
        return redirect('empleados')  # Puedes redirigir a una página de error o renderizar una plantilla de error específica

    empleado.delete()
    messages.success(request, f'Empleado {empleado} eliminado correctamente.')
    return redirect('empleados')

