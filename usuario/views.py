# usuario/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse

def user_home(request):
    return render(request, 'usuario/home.html')

def actualizar_usuario(request):
    if request.method == 'POST':
        # Aquí puedes manejar la lógica para actualizar la información del usuario.
        # Por ejemplo, puedes capturar los datos del formulario:
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        # Lógica para actualizar los datos en la base de datos
        # Por ahora, simularemos que la actualización fue exitosa.
        
        # Redirigir o mostrar un mensaje de éxito
        return HttpResponse("La información del usuario ha sido actualizada correctamente.")
    else:
        return HttpResponse("Método no permitido.", status=405)
