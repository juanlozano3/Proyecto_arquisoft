# usuario/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_home, name='user_home'),
    path('actualizar/', views.actualizar_usuario, name='actualizar_usuario'),  # Nueva ruta para la vista 'actualizar_usuario'
]
