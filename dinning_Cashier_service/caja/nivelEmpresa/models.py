from django.db import models

# Create your models here.


class Empresa(models.Model):

    nombre = models.CharField(max_length=20)
    direccion = models.CharField(max_length=20)
    razonSocial = models.CharField(max_length=20)
    siglas = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

    def __str__(self):
        return self.nombre


class Sucursal(models.Model):

    nombreSuc = models.CharField(max_length=20)
    direccion = models.CharField(max_length=20)
    telforno = models.CharField(max_length=20)
    empresa = models.ForeignKey("Empresa")

    class Meta:
        verbose_name = "Sucursal"
        verbose_name_plural = "Sucursales"

    def __str__(self):
        return self.nombreSuc
