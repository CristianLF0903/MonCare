from rest_framework import viewsets
from base.models import Dispositivo_Medico, Medicion
from .serializer import DispositivoMedicoSerializer, MedicionSerializer

# Create your views here.


class MedicionViewSet(viewsets.ModelViewSet):
    queryset = Medicion.objects.all()
    serializer_class = MedicionSerializer


class DispositivoMedicoViewSet(viewsets.ModelViewSet):
    queryset = Dispositivo_Medico.objects.all()
    serializer_class = DispositivoMedicoSerializer
