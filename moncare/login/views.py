from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from login.forms import LoginForm, RegistroForm


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['Correo']
            password = form.cleaned_data['Contraseña']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('login/home.html')
    else:
        form = LoginForm()

    return render(request, 'login/login.html', {'form': form})


def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Redirige a la página que desees después del registro exitoso
            return redirect('')
    else:
        form = RegistroForm()

    return render(request, 'login/registro.html', {'form': form})
