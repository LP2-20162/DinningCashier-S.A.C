from django.contrib import admin
from caja.models import Registro


class RegistroAdmin(admin.ModelAdmin):
    list_display = ("RegistroAnual",)
admin.site.register(Registro, RegistroAdmin)


# Register your models here.
