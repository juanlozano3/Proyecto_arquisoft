from django.contrib import admin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'email', 'login', 'phone')  # Campos que se mostrarán en la lista
    search_fields = ('nombre', 'email', 'login')  # Campos que se pueden buscar en el panel de administración
