"""
  TERMS OF USE - 

  Open Source 
 
 Copyright © 2022 Carlos M. Gómez Escobar
"""
from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
from django.db.models import Sum
from django.shortcuts import reverse





# Opciones de Pago. / / (DONE)

PAYMENT_CHOICES = (
	('PG', 'Pago Movil'),
	('E',  'Efectivo'),
	('P',  'Punto')
)

# Categorias de Opciones. / / (DONE)
CATEGORY_CHOICES = (
	('Ferreteria', 'Ferreteria'),
	('Alimentos', 'Alimentos'),
	('Salud', 'Salud'),
	('Tendencia', 'Tendencia'),
	('Otros', 'Otros')
)




# Producto. / (DONE)

class Producto(models.Model):
	id_producto = models.AutoField(primary_key=True)
	titulo = models.CharField(max_length=100)
	categoria = models.CharField(choices=CATEGORY_CHOICES, max_length=20)
	descripcion = models.TextField(default='', blank=True)

	def __str__(self):
		return f'{self.id_producto}- {self.titulo}- {self.categoria} {self.descripcion}'

class Item(models.Model):
	id_item = models.AutoField(primary_key=True)
	item = models.ForeignKey(Producto, on_delete=models.CASCADE, blank=True, null=True)
	precio = models.PositiveIntegerField(null=True)

	
	def __str__(self):
		return f'{self.id_item}- {self.item}- {self.precio}'
  
#Proveedores / (DONE)

class Proveedor(models.Model):
	id_proveedor = models.AutoField(primary_key=True)
	razon_social = models.CharField(max_length=70)
	direccion = models.CharField(max_length=200)
	telefono = models.CharField(max_length=30)
	email = models.EmailField(max_length=50, null=True)

	def __str__(self):
		return f'{self.id_proveedor}- {self.razon_social}- {self.telefono}- {self.email}'


#Stock "Proveedor + Item"  / (DONE)

class Stock(models.Model):
	id_stock = models.AutoField(primary_key=True)
	producto = models.ForeignKey(Producto, on_delete=models.CASCADE, blank=True, null=True)
	id_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, blank=True, null=True)
	costo = models.DecimalField(max_digits=9, decimal_places=2)
	cantidad = models.IntegerField(default=1)
	fecha= models.DateField(auto_now_add=True)

	
	def __str__(self):
		return f'{self.id_stock}- {self.producto}-  {self.id_proveedor}- {self.costo}- {self.cantidad}- {self.fecha}'

	def get_stock_item(self):
		return self.costo * self.cantidad

	def get_total_stock(self):
		total = 0
		for order_item_stock in self.producto.all():
			total += order_item_stock.get_stock_item()
		return total
	
	# @staticmethod  
	# def insertfactura(id_stock, id_proveedor, producto, costo, cantidad, fecha):  
	# 	cur = connection.cursor()  
	# 	cur.callproc('insertfactura', [id_stock, id_proveedor, producto, costo, cantidad, fecha])  
	# 	results = cur.fetchall() 
	# 	cur.close()
	# 	return results
	# @staticmethod  
	# def deleteFactura(idfactura):  
	# 	cur = connection.cursor()  
	# 	cur.callproc('deleteFactura', [idfactura])  
	# 	cur.close()


		

#Cliente / / (DONE)

class Cliente(models.Model):
	ci = models.CharField(primary_key=True,max_length=13)
	nombre = models.CharField(max_length=100,  blank=True, null=True)
	apellidos = models.CharField(max_length=100,  blank=True, null=True)
	direccion = models.CharField(max_length=200,  blank=True, null=True)
	telefono = models.CharField(max_length=100,  blank=True, null=True)
	email= models.EmailField()

	def __str__(self):
		return f'{self.ci}- {self.nombre}- {self.apellidos}- {self.direccion}- {self.telefono}- {self.email}' 


#Ordenes de Servicios "Pay, Checkout, Otros " /

	#Buscar los valores de matematicos de una factura:
		# Get_total_price_sumatoriaTotal, Get_total, 
		# Factura
		# Ordenes
		# 
		#



class OrdenItem(models.Model):
	id_orden_items= models.AutoField(primary_key=True)
	item = models.ForeignKey(Item, on_delete=models.CASCADE, blank=True, null=True)
	precio = models.DecimalField(max_digits=9, decimal_places=2)
	cantidad = models.IntegerField(default=1)
	fecha = models.DateField(auto_now_add=True)
	ordered = models.BooleanField(default=False)

	def __str__(self):
		return f'{self.id_orden_items}- {self.item }-{self.precio  }- {self.cantidad }- {self.fecha }- {self.ordered }' 


	def get_item_precio(self):
		return self.cantidad * self.item.precio

	def get_total(self):
		total = 0
		for order_item in self.item.all():
			total += order_item.get_item_precio()
		return total

	    

	    
	  
class Orden(models.Model):
	id_orden = models.AutoField(primary_key=True)
	cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, blank=True, null=True)
	items = models.ManyToManyField(OrdenItem)
	fecha_pago = models.DateTimeField(auto_now_add=True)
	pago_opciones = models.CharField(choices=PAYMENT_CHOICES, max_length=20)
	

	def __str__(self):
	    return f'{self.id_orden}- {self.cliente }- {self.fecha_pago}- {self.pago_opciones}'

	
	
		
