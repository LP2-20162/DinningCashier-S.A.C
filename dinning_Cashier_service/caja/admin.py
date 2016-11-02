from django.contrib import admin
from caja.models import User, Registro

admin.site.register(User)


class RegistroAdmin(admin.ModelAdmin):
    list_display = ("RegistroAnual",)
admin.site.register(Registro, RegistroAdmin)
