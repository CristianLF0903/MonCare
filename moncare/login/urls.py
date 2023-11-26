from django.contrib import admin
from django.urls import path
from login.views import registro, iniciar_sesion

urlpatterns = [
    path('', iniciar_sesion, name='login'),
    path('registro/', registro, name='registro'),
]
