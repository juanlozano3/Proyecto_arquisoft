from django.db import models

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    login = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)  # O cambia 'password' a 'Password' si prefieres usar el nombre exacto de la imagen

    def __str__(self):
        return self.nombre
