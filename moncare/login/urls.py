from django.urls import path
from login.views import login_view, registro_view

urlpatterns = [
    path('', login_view, name='login'),
    path('register/', registro_view, name='register'),
]
