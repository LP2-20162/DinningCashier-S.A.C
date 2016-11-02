from django.contrib import admin
<<<<<<< HEAD:dinning_Cashier_service/caja/usuario/admin.py
from .models import User
=======
from caja.models import User, Registro
>>>>>>> 8d1aacd578030dcef59f4201e00dbab7f631ec03:dinning_Cashier_service/caja/admin.py

admin.site.register(User)


class RegistroAdmin(admin.ModelAdmin):
    list_display = ("RegistroAnual",)
admin.site.register(Registro, RegistroAdmin)
