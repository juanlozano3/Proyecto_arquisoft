# usuario/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Usuario
from .logic.usuario_logic import actualizar_usuario_logic

def homepage(request):
    return render(request, 'homepage.html')

def user_home(request):
    usuario = get_object_or_404(Usuario, id=1)  # Replace 1 with the appropriate ID or fetch dynamically
    return render(request, 'usuario/user_home.html', {'usuario': usuario})

def actualizar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        usuario.nombre = request.POST.get('username')
        usuario.email = request.POST.get('email')
        usuario.phone = request.POST.get('phone')
        usuario.save()
        return redirect('user_home')
    return render(request, 'actualizar_usuario.html', {'usuario': usuario})

def health_check(request):
    return HttpResponse("OK")