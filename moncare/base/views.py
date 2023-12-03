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
def logout_view(request):
    logout(request) #Usuario logueado
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
            'accion': 'Gestor',
            'entidad': 'de dispositivos',
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

        return render(request, 'base/gestor-empleados.html', {'empleados': empleados, 'accion': 'Gestor', 'entidad': 'de Empleados'})

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

#Pacientes_views
@login_required
def pacientes(request):
    user_logged = request.user
    if user_logged.tipo_usuario == 'Empleado de Salud':
        pacientes = list(user_logged.pacientes.all().values_list('id','first_name','last_name'))

        return render(request, 'base/gestor-pacientes.html', {'pacientes': pacientes, 'accion': 'Gestor', 'entidad': 'de pacientes'})

    else:
        messages.error(request, 'No tienes acceso a esta vista')
        return redirect('pagina_principal')

@login_required
def agregar_paciente1(request):
    user_logged = request.user
    pacientes = list(Usuario.objects.filter(tipo_usuario='Paciente', tiene_medico=False).values_list('id','first_name','last_name', 'email'))

    return render(request, 'base/gestor-pacientes.html', {'pacientes': pacientes, 'accion': 'Agregar', 'entidad': 'paciente'})

@login_required
def agregar_paciente(request, paciente_id):
    user_logged = request.user
    try:
        paciente = get_object_or_404(Usuario, id=paciente_id)
    except paciente.DoesNotExist:
        messages.error(request, 'Hubo un error, no se encontró el usaurio.')
        return redirect('pacientes')  # Puedes redirigir a una página de error o renderizar una plantilla de error específica
    
    paciente.tiene_medico = True
    paciente.save()

    user_logged.pacientes.add(paciente)
    user_logged.save()

    messages.success(request, 'El usuario se agrego correctamente como paciente.')
    return redirect('pacientes')  # Puedes redirigir a una página de error o renderizar una plantilla de error específica

@login_required
def detalles_paciente(request, paciente_id):
    try:
        paciente = get_object_or_404(Usuario, id=paciente_id)
    except paciente.DoesNotExist:
        messages.error(request, 'Hubo un error, no se encontró el usaurio.')
        return redirect('pacientes')

    cuidador = Usuario.objects.filter(tipo_usuario='Empleado de Salud', tipo_empleado='Cuidador', pacientes=paciente).first()
    historia_clinica = Historia_Clinica.objects.filter(paciente = paciente)
    dispositivos = Dispositivo_Medico.objects.filter(id_paciente = paciente).values_list('id', 'referencia', 'marca')

    #registros = Registro.objects.filter(id_historia_clinica = historia_clinica)
    registros = Registro.objects.all()
    
    return render(request, 'base/detalles-paciente.html', {'paciente':paciente, 'HC':historia_clinica, 'dispositivos': dispositivos, 'cuidador': cuidador, 'registros':registros})

@login_required
def eliminar_paciente(request, paciente_id):
    user_logged = request.user
    try:
        paciente = get_object_or_404(Usuario, id=paciente_id)
    except paciente.DoesNotExist:
        messages.error(request, 'Hubo un error, no se encontró el usaurio.')
        return redirect('pacientes')  # Puedes redirigir a una página de error o renderizar una plantilla de error específica
    
    paciente.tiene_medico = False
    paciente.save()

    user_logged.pacientes.remove(paciente)
    user_logged.save()

    messages.success(request, 'El usuario se agrego correctamente como paciente.')
    return redirect('pacientes')  # Puedes redirigir a una página de error o renderizar una plantilla de error específica

@login_required
def agregar_dispositivo_paciente(request, paciente_id, dispositivo_id):
    user = request.user
    try:
        dispositivo = get_object_or_404(Dispositivo_Medico, id=dispositivo_id)
    except dispositivo.DoesNotExist:
        messages.error(request, 'Hubo un error, no se encontró el dispositivo.')
        return redirect('detalles_paciente', paciente_id)  # Puedes redirigir a una página de error o renderizar una plantilla de error específica

    dispositivo.id_paciente = Usuario.objects.get(id=paciente_id)
    dispositivo.id_configurador = user
    dispositivo.asignado = True
    dispositivo.save()

    messages.success(request, 'El dispositivo se agrego correctamente.')
    return redirect('detalles_paciente', paciente_id)  # Puedes redirigir a una página de error o renderizar una plantilla de error específica
    

@login_required
def agregar_dispositivo_p(request, paciente_id):

    dispositivos = list(Dispositivo_Medico.objects.filter(asignado=False).values_list('id', 'referencia', 'marca'))


    return render(request, 'base/gestor-dispositivos.html', {'dispositivos': dispositivos, 'accion': 'Agregar', 'entidad': 'dispositivo a paciente', 'paciente': paciente_id})

@login_required
def eliminar_dispositivo_p(request, dispositivo_id):

    dispositivo = Dispositivo_Medico.objects.get(id = dispositivo_id)
    paciente = dispositivo.id_paciente.id

    dispositivo.id_configurador = None
    dispositivo.id_paciente = None
    dispositivo.asignado = False
    dispositivo.save()

    return redirect('detalles_paciente', paciente)

@login_required
def eliminar_cuidador_p(request, paciente_id, cuidador_id):

    cuidador = Usuario.objects.get(id = cuidador_id)
    paciente = Usuario.objects.get(id = paciente_id)

    cuidador.pacientes.remove(paciente)
    cuidador.save()

    messages.success(request, 'El cuidador se elimino correctamente.')
    return redirect('detalles_paciente', paciente_id)

@login_required
def agregar_cuidador_p(request, paciente_id):

    empleados = list(Usuario.objects.filter(tipo_usuario = 'Empleado de Salud',tipo_empleado='Cuidador', is_admin=False).values_list('id','first_name','last_name', 'email', 'tipo_empleado'))


    return render(request, 'base/gestor-empleados.html', {'empleados': empleados, 'accion': 'Agregar', 'entidad': 'cuidador a paciente', 'paciente': paciente_id})

@login_required
def agregar_cuidador_paciente(request, paciente_id, cuidador_id):
    user = request.user
    try:
        cuidador = get_object_or_404(Usuario, id=cuidador_id)
        paciente = get_object_or_404(Usuario, id = paciente_id)
    except paciente.DoesNotExist or cuidador.DoesNotExist:
        messages.error(request, 'Hubo un error, no se encontró el usuario.')
        return redirect('detalles_paciente', paciente_id)  # Puedes redirigir a una página de error o renderizar una plantilla de error específica

    cuidador.pacientes.add(paciente)
    cuidador.save()

    messages.success(request, 'El cuidador se asigno correctamente.')
    return redirect('detalles_paciente', paciente_id)  # Puedes redirigir a una página de error o renderizar una plantilla de error específica
    

#Familiar
@login_required
def familiares(request):
    user = request.user

    familiares = user.familiares.all()

    accion = 'Gestor'
    
    return render(request, 'base/gestor-familiares.html', {'personas': familiares, 'accion': accion, 'entidad': 'de Familiares'})

@login_required
def elimiar_persona(request, familiar_id):
    user = request.user
    try:
        familiar = get_object_or_404(Usuario, id=familiar_id)
    except familiar.DoesNotExist:
        messages.error(request, 'Hubo un error, no se encontró el usuario.')
        return redirect('familiares') 
    
    familiar.familiares.remove(user)
    familiar.save()
    user.familiares.remove(familiar)
    user.save()

    messages.success(request, 'El familiar se elimino correctamente.')
    return redirect('familiares')  # Puedes redirigir a una página de error o renderizar una plantilla de error específica

@login_required
def agregar_familiar(request):
    user = request.user
    familiares = Usuario.objects.filter(tipo_usuario='Familiar').exclude(id__in=user.familiares.all())

    return render(request, 'base/gestor-familiares.html', {'personas': familiares, 'accion': 'Agregar', 'entidad': 'Familiar'})

@login_required
def asignar_persona(request, familiar_id):
    user = request.user
    try:
        familiar = get_object_or_404(Usuario, id=familiar_id)
    except paciente.DoesNotExist or cuidador.DoesNotExist:
        messages.error(request, 'Hubo un error, no se encontró el usuario.')
        return redirect('familiares')  # Puedes redirigir a una página de error o renderizar una plantilla de error específica

    familiar.familiares.add(user)
    familiar.save()
    user.familiares.add(familiar)
    user.save()

    messages.success(request, 'El familiar se asigno correctamente.')
    return redirect('familiares')