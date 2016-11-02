from django.db import models

# Create your models here.


class UsuarioCajero(models.Model):

    nombre = models.CharField(max_length=20)
    usuario = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20, null=True, blank=True)
    perfi = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    sucursal = models.CharField(max_length=20)

    class Meta:
        verbose_name = "UsuarioCajero"
        verbose_name_plural = "UsuarioCajeros"

    def __str__(self):
        return self.nombre
