# usuario/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse

def homepage(request):
    return render(request, 'home.html')

def user_home(request):
    return render(request, 'usuario/home.html')

def actualizar_usuario(request):
    if request.method == 'POST':
        # Aquí puedes agregar la lógica para actualizar la información del usuario
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        # Simulación de una actualización exitosa
        return HttpResponse("La información del usuario ha sido actualizada correctamente.")
    else:
        return HttpResponse("Método no permitido.", status=405)
