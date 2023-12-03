from django.urls import path, include
from rest_framework import routers
from API import views

router = routers.DefaultRouter()
router.register(r'dispositivo_medico', views.DispositivoMedicoViewSet)
router.register(r'medicion', views.MedicionViewSet)

urlpatterns = [
    path('', include(router.urls))
]
