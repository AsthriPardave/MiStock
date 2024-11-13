from django.contrib import admin
from .models import *

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id','apellido','nombre','numero', 'deudor')

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'correo')

class BoletaAdmin(admin.ModelAdmin):
    list_display = ('id', 'fechaHora', 'pagado', 'cliente', 'venta')

class ProductosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'stock', 'precio', 'estado')

class VentasAdmin(admin.ModelAdmin):
    list_display = ('id', 'cantProductos', 'precioTotal', 'producto')

class PagoAdmin(admin.ModelAdmin):
    list_display = ('id', 'medioPago', 'precio', 'boleta')

# Register your models here.

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Boleta, BoletaAdmin)
admin.site.register(Productos, ProductosAdmin)
admin.site.register(Ventas, VentasAdmin)
admin.site.register(Pago, PagoAdmin)