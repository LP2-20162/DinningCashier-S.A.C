from django.contrib import admin

from .models import Caja


class CajaAdmin(admin.ModelAdmin):
    list_display = ("concepto", "sucursal",)
    search_fields = ("concepto", "sucursal",)
    list_per_page = 2

admin.site.register(Caja, CajaAdmin)
