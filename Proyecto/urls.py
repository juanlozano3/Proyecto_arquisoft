"""Proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Proyecto/urls.py
from django.contrib import admin
from django.urls import path
from usuario import views  # Importa las vistas desde la aplicación 'usuario'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),  # Ruta para la página principal
    path('usuario/', views.user_home, name='user_home'),  # Ruta para la vista de usuario
    path('usuario/actualizar/', views.actualizar_usuario, name='actualizar_usuario'),  # Nueva ruta para la vista 'actualizar_usuario'
    path("health-check/", views.health_check),
]
