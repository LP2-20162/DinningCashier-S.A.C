from django.contrib import admin

from cajaIngreso.models import Caja


class CajaAdmin(admin.ModelAdmin):
    list_display = ("concepto", "precio",)
    search_fields = ("concepto", "precio",)
    list_per_page = 2

admin.site.register(Caja, CajaAdmin)
