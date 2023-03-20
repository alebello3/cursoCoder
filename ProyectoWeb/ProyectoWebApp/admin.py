from django.contrib import admin

from ProyectoWebApp.models import Clientes, Articulos, pedidos


# Register your models here.
class ClientesAdmin(admin.ModelAdmin):
    list_display=("nombre", "direccion", "correo", "telefono")
    search_fields=("nombre", "direccion", "correo", "telefono")

admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Articulos)
admin.site.register(pedidos)



