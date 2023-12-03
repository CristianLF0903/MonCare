from django.urls import path, include
from rest_framework import routers
from API.views import MedicionViewSet, DispositivoMedicoViewSet

router = routers.DefaultRouter()
router.register(r'dispositivo_medico', DispositivoMedicoViewSet)
router.register(r'medicion', MedicionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
