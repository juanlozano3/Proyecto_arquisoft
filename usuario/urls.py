# usuario/urls.py
from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.user_home, name='user_home'),
    path('actualizar/', views.actualizar_usuario, name='actualizar_usuario'),  # Incluye el id en la URL
    path("health-check/", views.health_check),
    path("admin/", admin.site.urls),

]
