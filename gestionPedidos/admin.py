from django.contrib import admin
from gestionPedidos.models import Clientes, Articulos, Pedidos
# Register your models here.

class clientesAdmin(admin.ModelAdmin):
    list_display=("nombre","email","tfno")
    search_fields=("nombre","tfno")

class articulosAdmin(admin.ModelAdmin):
    list_filter=("seccion",)

class pedidosAdmin(admin.ModelAdmin):
    list_display=("numero","fecha")
    list_filter=("fecha",)
    date_hierarchy="fecha"


admin.site.register(Clientes,clientesAdmin)
admin.site.register(Articulos,articulosAdmin)
admin.site.register(Pedidos,pedidosAdmin)

