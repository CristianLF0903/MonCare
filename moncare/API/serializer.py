from rest_framework import serializers
from base.models import Dispositivo_Medico, Medicion


class MedicionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicion
        fields = ('id', 'parametro', 'valor', 'unidades', 'id_dispositivo')


class DispositivoMedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispositivo_Medico
        fields = ('id', 'api_key', 'referencia', 'marca')
