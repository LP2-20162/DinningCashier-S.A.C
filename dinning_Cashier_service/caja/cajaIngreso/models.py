from django.db import models

# Create your models here.


class Caja(models.Model):

    concepto = models.CharField(max_length=60)
    anulado = models.BooleanField(default=True)
    cuentaEmpresa = models.IntegerField(default=170)
    cuentaCliente = models.IntegerField(default=170)
    cuentaGanancia = models.IntegerField(default=170)
    cuentaVenta = models.IntegerField(default=170)
    #numDocumento = models.CharField(max_lenght=9, null=True, blank=True)
    entregadoA = models.CharField(max_length=60, null=True, blank=True)
    fecha = models.DateTimeField(max_length=60, null=True, blank=True)
    #precio = models.DecimalField(max_digits=5)
    sucursal = models.IntegerField(default=170)
    total = models.CharField(max_length=60, null=True, blank=True)

    class Meta:
        verbose_name = "Caja"
        verbose_name_plural = "Cajas"

    def __str__(self):
        return self.concepto
