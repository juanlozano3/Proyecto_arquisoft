from django.contrib import admin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'email', 'login')  # 'phone' eliminado de la lista
    search_fields = ('nombre', 'email', 'login')