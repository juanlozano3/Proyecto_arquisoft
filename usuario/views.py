# usuario/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Usuario
from .logic.usuario_logic import actualizar_usuario_logic
def homepage(request):
    return render(request, 'home.html')

def user_home(request):
    usuario = get_object_or_404(Usuario, id=1)  # Cambia `1` por el ID del usuario actual
    return render(request, 'usuario/home.html', {'usuario': usuario})

def actualizar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        usuario.nombre = request.POST.get('username')
        usuario.email = request.POST.get('email')
        usuario.phone = request.POST.get('phone')
        usuario.save()
        return redirect('user_home')
    return render(request, 'usuario/actualizar_usuario.html', {'usuario': usuario})

def health_check(request):
    return HttpResponse("OK")