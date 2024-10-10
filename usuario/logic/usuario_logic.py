from usuario.models import Usuario

def actualizar_usuario_logic(id, nombre, email, login, password):
    try:
        # Buscar el usuario por ID
        usuario = Usuario.objects.get(id=id)
        # Actualizar los campos del usuario
        usuario.nombre = nombre
        usuario.email = email
        usuario.login = login
        usuario.password = password
        usuario.save()
        return True, "La información del usuario ha sido actualizada correctamente."
    except Usuario.DoesNotExist:
        return False, "El usuario no existe."
    except Exception as e:
        return False, f"Error al actualizar el usuario: {str(e)}"
