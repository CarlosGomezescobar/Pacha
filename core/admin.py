"""
  TERMS OF USE - 

  Open Source 
 
 Copyright © 2022 Carlos M. Gómez Escobar
"""
from django.contrib import admin
from core.models import *





class ProveedorAdmin(admin.ModelAdmin):
	list_display=('id_proveedor', 'razon_social', 'direccion', 'telefono', 'email')
	list_filter=("id_proveedor", "razon_social" )
	search_fields=("id_proveedor","razon_social" ,"direccion", "category")


class ProductoAdmin(admin.ModelAdmin):
	list_display=('id_producto', 'titulo', 'categoria', 'descripcion')
	list_filter=("id_producto", "titulo", "categoria")
	search_fields=("id_producto", "titulo")

class ItemAdmin(admin.ModelAdmin):
	list_display=('id_item', 'item',  'precio')
	list_filter=("item", "precio")
	search_fields=("item", "precio")

class StockAdmin(admin.ModelAdmin):
	list_display=('id_stock', 'producto', 'id_proveedor', 'costo', 'cantidad','fecha')
	list_filter=("id_proveedor", "fecha")
	search_fields=("id_stock", "producto", "id_proveedor")


class ClienteAdmin(admin.ModelAdmin):
	list_display=('ci', 'nombre', 'apellidos', 'direccion', 'telefono', 'email')
	list_filter=("ci", "nombre", "apellidos")
	search_fields=("ci", "nombre", "apellidos")

class OrdenItemAdmin(admin.ModelAdmin):
	
	list_display=('id_orden_items', 'ordered', 'item', 'precio', 'cantidad', 'fecha')
	list_filter=("id_orden_items", "ordered")
	search_fields=("id_orden_items", "ordered")

class OrdenAdmin(admin.ModelAdmin):
	
	list_display=('id_orden', 'cliente',  'fecha_pago', 'pago_opciones')
	list_filter=("id_orden", "cliente", "fecha_pago")
	search_fields=("id_orden", "cliente")



admin.site.register(Cliente,  ClienteAdmin)
admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Producto,  ProductoAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(OrdenItem, OrdenItemAdmin)
admin.site.register(Orden, OrdenAdmin)

# admin.site.register(PAYMENT_CHOICES)
# admin.site.register(CATEGORY_CHOICES)



