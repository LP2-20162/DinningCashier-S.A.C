from django.db import models


class Registro(models.Model):

    registroAnual = models.CharField(max_length=60, null=True, blank=True)

    class Meta:
        verbose_name = "Registro"
        verbose_name_plural = "Registros"

    def __str__(self):
        return self.registroAnual

# Create your models here.
