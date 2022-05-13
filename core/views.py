"""
  TERMS OF USE - 

  Open Source 
 
 Copyright © 2022 Carlos M. Gómez Escobar
"""
from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.models import User
from django.db.models import F, Count, Max
from django.utils import timezone
import csv
import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .forms import *
from django.views.generic import ListView, DetailView, View
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.db.models import query
from django.conf import settings
from django.http import HttpResponse, response
from django.db.models import F, Count, Max


datoscompany={'dir':"Barinas",'suc':'Alto Barinas','ruc':'00000000000'}
dias_vencimiento_proforma=7
facturaNusuario=False

def is_valid(values):
    valid = True
    for field in values:
        if field == '':
            valid = False
    return valid

def Index(request):

	return render(request, 'index.html')

@login_required
def Home(request):
	proveedor = Proveedor.objects.all().count()
	productos = Producto.objects.all().count()
	cliente = Cliente.objects.all().count()
	workers_count = User.objects.all().count()

	context = {
			"proveedor": proveedor,
			"productos": productos,
			"cliente": cliente,
			"workers_count": workers_count,
	}

	return render(request, 'home.html', context)

		# definir en el html un sub Navbar de los Proveedores, Clinetes, Productos (COUNT)
		# Cuadros de enlaces para las diferentes Sites


#Producto Views:

def add_productos(request):
	form = ProductoForm(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request, 'Agregado Sastifactoriamente ')
		return redirect ('/list_productos')

	context = {
		"form": form,
		"title": "Agregar Producto",
	}

	return render(request, "custom/add_producto.html", context)

def delete_productos(request,pk):
	queryset = Producto.objects.get(pk=pk)
	if request.method == 'POST':
		queryset.delete()
		messages.success(request, 'Borrado Sastifactoriamente')
		return redirect('/list_productos')
	return render (request, "custom/delete_producto.html")

def update_productos(request, pk):
	queryset =  Producto.objects.get(pk=pk)
	form = UpdateProductoForm(instance=queryset)
	if  request.method == 'POST':
		form = UpdateProductoForm(request.POST, instance=queryset)
		
		if form.is_valid():
			form.save()
			messages.success(request, 'Actualizacion Sastifactoriamente')
			return redirect ('/list_productos')
	context ={
		"form": form,
	}
	return render(request, "custom/add_producto.html", context)

def list_productos(request):
	header = 'List of Cliente'
	form = SearchProductoForm(request.POST or None)
	queryset = Producto.objects.all()

	context = {
		"form": form,
		"header": header,
		"queryset": queryset,
	}
		
	if  request.method == 'POST':
		queryset = Producto.objects.filter(titulo__icontains=form['titulo'].value()
											#categoria__icontains=form['categoria'].value(), 
										)
			
		if form['export_to_CSV'].value() == True:
			response = HttpResponse(content_type='text/csv')




			response['Content-Disposition'] =  'attachment; filename="List of Clients.csv"'
			writer =csv.writer(response)
			writer.writerow(['ID_PRoDUCTO','TITULO', 'CATEGORIA', 'DESCRIPCION'])
			instance = queryset
			for prod in instance:
				writer.writerow([prod.id_producto, prod.titulo, prod.categoria, prod.descripcion])
			return response

		context = {
			"form": form,
			"header": header,
			"queryset": queryset,
	}

	return render(request, "custom/list_producto.html", context)



#Cliente Views:

def add_clientes(request):
	form = ClienteForm(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request, 'Agregado Sastifactoriamente ')
		return redirect ('/list_clientes')

	context = {
		"form": form,
		"title": "Agregar cliente",
	}

	return render(request, "cliente/add_cliente.html", context)

def delete_clientes(request,pk):
	queryset = Cliente.objects.get(pk=pk)
	if request.method == 'POST':
		queryset.delete()
		messages.success(request, 'Borrado Sastifactoriamente')
		return redirect('/list_clientes')
	return render (request, "cliente/delete_cliente.html")

def update_clientes(request, pk):
	queryset =  Cliente.objects.get(pk=pk)
	form = UpdateClienteForm(instance=queryset)
	if  request.method == 'POST':
		form = UpdateClienteForm(request.POST, instance=queryset)
		
		if form.is_valid():
			form.save()
			messages.success(request, 'Actualizacion Sastifactoriamente')
			return redirect ('/list_clientes')
	context ={
		"form": form,
	}
	return render(request, "cliente/add_cliente.html", context)

def list_clientes(request):
	header = 'List of Cliente'
	form = SearchClienteForm(request.POST or None)
	queryset = Cliente.objects.all()

	context = {
		"form": form,
		"header": header,
		"queryset": queryset,
	}
		
	if  request.method == 'POST':
		queryset = Cliente.objects.filter(ci__icontains=form['ci'].value() 
										)
			
		if form['export_to_CSV'].value() == True:
			response = HttpResponse(content_type='text/csv')

			response['Content-Disposition'] =  'attachment; filename="List of Clients.csv"'
			writer =csv.writer(response)
			writer.writerow(['CI', 'NOMBRE', 'APELLIDO', 'DIRECCION', 'TELEFONO', 'EMAIL'])
			instance = queryset
			for cliente in instance:
				writer.writerow([cliente.ci, cliente.nombre, cliente.apellido, cliente.direccion, cliente.telefono, cliente.email])
			return response

		context = {
			"form": form,
			"header": header,
			"queryset": queryset,
	}

	return render(request, "cliente/list_cliente.html", context)


#Proveedor Views:  


#Check
def add_proveedores(request):
	form = ProveedorForm(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request, 'Agregado Sastifactoriamente ')
		return redirect ('/list_proveedores')

	context = {
		"form": form,
		"title": "Agregar Proveedor",
	}

	return render(request, "proveedor/add_proveedor.html", context)

def delete_proveedores(request,pk):
	queryset = Proveedor.objects.get(pk=pk)
	if request.method == 'POST':
		queryset.delete()
		messages.success(request, 'Borrado Sastifactoriamente')
		return redirect('/list_proveedores')
	return render (request, "proveedor/delete_proveedor.html")

def update_proveedores(request, pk):
	queryset =  Proveedor.objects.get(pk=pk)
	form = UpdateProveedorForm(instance=queryset)
	if  request.method == 'POST':
		form = UpdateProveedorForm(request.POST, instance=queryset)

		if form.is_valid():
			form.save()
			messages.success(request, 'Actualizacion Sastifactoriamente')
			return redirect ('/list_proveedores')
	context ={
		"form": form,
	}
	return render(request, "proveedor/add_proveedor.html", context)

#check:  por hacer link to factura del proveedor
def list_proveedores(request):
	header = 'Lista de Proveedores'
	form = SearchProveedorForm(request.POST or None)
	queryset = Proveedor.objects.all()

	context = {
			"form": form,
			"header": header,
			"queryset": queryset,
	}

	if  request.method == 'POST':
		queryset = Proveedor.objects.filter(razon_social__icontains=form['razon_social'].value() 
											)
			
		if form['export_to_CSV'].value() == True:
			response = HttpResponse(content_type='text/csv')

			response['Content-Disposition'] =  'attachment; filename="Lista de Proveedores.csv"'
			writer =csv.writer(response)
			writer.writerow(['ID_PROVEEDOR', 'RAZON_SOCIAL', 'APELLIDO', 'DIRECCION', 'TELEFONO', 'EMAIL'])
			instance = queryset
			for proveedor in instance:
				writer.writerow([proveedor.id_proveedor, proveedor.razon_social, proveedor.direccion, proveedor.telefono, proveedor.email])
			return response

		context = {
			"form": form,
			"header": header,
			"queryset": queryset,
	}

	return render(request, "proveedor/list_proveedor.html", context)


def invoice_stock(request, self, pk):

	queryset = Proveedor.objects.all()
	stock = Stock.objects.get(pk=pk)
	total_item = Stock.objects.annotate(get_stock_item=Count(self.cantidad) * Count(self.costo))
	get_total_stocks = Stock.objects.filter(get_total_stock=request.GET.get('get_total_stock'))
	fecha=str(datetime.datetime.now()) 
	maxNfactura= Stock.objects.all().aggregate(Max('id_stock'))['id_stock__max']
	proveedor_form = SearchProveedorForm(request.POST or None)
	stock_form = StockForm(request.POST or None)

	if proveedor_form.is_valid() and stock_form.is_valid():
		proveedor_form.save()
		stock_form.save()


	context = {
		"stock": stock,
		"fecha": fecha,
		"company": datoscompany,
		"Nfactura": int(maxNfactura+1),
		"items_orden": "items_orden",
		"total_item": total_item,
		"get_total_stocks": get_total_stocks,
		"queryset": queryset,
		"stock_form": stock_form,
		"proveedor_form": proveedor_form,

	}

	if request.GET.get('nombreproveedor'):
		idfactura= Stock.insertfactura(request.GET.get('facturaN') ,request.GET.get('fechaF'), request.GET.get('pretotal'))[0][0]
		cantfl=request.GET.get('nLineas').split(':')
		for i in cantfl:
			idproducto=Producto.objects.filter(descripcion=request.GET.get('descripcion'+i))[0].id_producto
			Stock.insertfactura(idfactura,idproducto,request.GET.get('cantidad'+i),request.GET.get('costo'+i),request.GET.get('total_linea'+i)) 
	return render(self.request, 'proveedor/orden_proveedor.html', context)
       

def list_invoice(request):
	facturas = Stock.objects.all()
	context = {
		"object_list": facturas,
		"tipo_objeto":"facturas",
	}
	return render(request, "order/list_invoice.html", context)
	



#Poducto Views: 

def List_Items(request, self):
	header = 'Lista de Productos'
	form = ItemSearchForm(request.POST or None)
	queryset = Item.objects.all()
		
		

	context = {
			"form": form,
			"header": header,
			"queryset": queryset,
				
				
	}
		
	if  request.method == 'POST':
		queryset = Item.objects.filter(#category__icontains=form['category'].value(), 
										nombre__icontains=form['titutlo'].value() 
										)
			
		if form['export_to_CSV'].value() == True:
			response = HttpResponse(content_type='text/csv')


			response['Content-Disposition'] =  'attachment; filename="Lista de Productos.csv"'
			writer =csv.writer(response)
			writer.writerow(['ID_ITEM', 'TITULO', 'CATEGORIA', 'PRECIO', 'DESCRIPCION'])
			instance = queryset
			for Product in instance:
				writer.writerow([Product.id_item, Product.titulo, Product.categoria, Product.precio, Product.description])
			return response

		context = {
			"form": form,
			"header": header,
			"queryset": queryset,
				
		}

	return render(request, "custom/list_items.html", context)




def update_items(request, pk):
	queryset =  Item.objects.get(pk=pk)
	form = ItemUpdapteForm(instance=queryset)
	if  request.method == 'POST':
		form = ItemUpdapteForm(request.POST, instance=queryset)

		if form.is_valid():
			form.save()
			messages.success(request, 'Actualizacion Sastifactoriamente')
			return redirect ('/list_Items')
	context ={
		"form": form,
	}
	return render(request, "custom/add_items.html", context)

def delete_items(request,pk):
	queryset = Item.objects.get(pk=pk)
	if request.method == 'POST':
		queryset.delete()
		messages.success(request, 'Borrado Sastifactoriamente')
		return redirect('/list_Items')
	return render (request, 'custom/delete_items.html')

def add_items(request):
	queryset =  Item.objects.all()
	form = ItemForm(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request, 'Agregado Sastifactoriamente ')
		return redirect ('/list_Items')

	context = {
		"form": form,
		"title": "Add Item",
		"queryset": queryset,
	}

	return render(request, "custom/add_items.html", context)


def stock_detail(request):
	queryset =  Stock.objects.all()
	form =  StockSearchForm(request.POST or None)
	get_total_stock_item = Stock.objects.annotate(
	   get_stock_item=Count('costo') * Count('cantidad'))
	if form.is_valid():
		form.save()
		
	context ={
			
		"queryset": queryset,
		"form": form,
		"get_total_stock_item ": get_total_stock_item, 

	}
	if  request.method == 'POST':
		queryset = Stock.objects.filter(#category__icontains=form['category'].value(), 
										nombre__icontains=form['id_producto'].value() 
										)
			
		if form['export_to_CSV'].value() == True:
			response = HttpResponse(content_type='text/csv')

			response['Content-Disposition'] =  'attachment; filename="List of Stock.csv"'
			writer =csv.writer(response)
			writer.writerow(['ID_PRODUCTO', 'CATEGORIA', 'ID_PROVEEDOR', 'COSTO', 'CANTIDAD', 'FECHA'])
			instance = queryset
			for stock in instance:
				writer.writerow([stock.id_producto, stock.categoria, stock.id_proveedor, stock.costo, stock.cantidad, stock.fecha])
			return response

	return render (request, 'custom/stock_detail.html', context)

		 
	
	


#Ordenes de Servicios:  
	#TODO: Factura Proveedor,Factura Cliente, Payment's Proveedor / Clientes
	#HTML 




def add_order(request, self):
	clientes_order = Cliente.objects.all()

	items = Item.objects.all()
	orden_item_all = OrdenItem.objects.all()
		

	get_total_item_lineal = OrdenItem.objects.annotate(
	   get_item_precio=Count('precio') * Count('cantidad'))

	   # get_total_orden_item = get_total_item_lineal.all()count()

	   
	    
	    
	cliente_form = ClienteForm(request.POST or None)
	orden_item_form = OrdenItemForm(request.POST or None)


	# cliente_form = self.request.GET.get('Cliente')
	#producto_form= self.request.GET.get('Producto')
	if cliente_form.is_valid() and orden_item_form.is_valid():
		cliente_form.save()
		orden_item_form.save()
		messages.success(request, 'Agregado Sastifactoriamente ')
		return redirect ('/list_order')

	context = {
		'clientes_orders': clientes_order,
		'items': items,
		'orden_item_all': orden_item_all,
		'orden_all':" ordenes_all",
		'get_total_item_lineal': get_total_item_lineal,
		'get_total_orden': "get_total_orden",
			
		'cliente_form': cliente_form,
		'orden_item_form': orden_item_form,
			
			
	}

	return render(request, "order/add_order.html", context)

def list_order(request, self):

	header = 'Lista de Ordenes'
	form =  OrdenItemSearchForm(request.POST or None)
	queryset = Orden.objects.all()
	ordenes = OrdenItem.objects.all()
		
		

	context = {
			"form": form,
			"header": header,
			"queryset": queryset,
			'ordenes': ordenes, 
				
				
	}
	if  request.method == 'POST':
		queryset = Orden.objects.filter(#category__icontains=form['category'].value(), 
										nombre__icontains=form['id.orden'].value(),
										# nombre__icontains=form['cliente'].value(),  
										)
		context = {
			"form": form,
			"header": header,
			"queryset": queryset,
			'ordenes': ordenes, 
				
				
		}
		

		

	return render(request, "order/list_order.html", context)


def delete_order(request,pk):
	queryset = OrdenItem.objects.get(pk=pk)
	if request.method == 'POST':
		queryset.delete()
		messages.success(request, 'Borrado Sastifactoriamente')
		return redirect('/list_order')
	return render (request, 'order/delete_order.html')


# def invoice_stock(request, self):
	# stock_all = Stock.objects.all()
	# stock_form = StockForm
	#Get_total_stock_prices = ------

	# 	context = {
	# 	'stock_form': stock_form,
	# 	'stock_all ': stock_all ,
	# 	
	# 	}
	# 	return render(request, "order/invoice_stock.html", context)



# def invoice(request, self):
	#   orden_all = Orden.objects.all()
	#   pago_orden = Pago_Orden.objects.all()

	# 	monto_total_pagar = Orden.objects.annotate(get_total_orden)
	# 	items = Item.objects.all()

	# 	cliente_form = ClienteForm(request.POST or None)

	# 	context = {
	# 	'cliente_form': cliente_form,
	# 	'monto_total_pagar':  monto_total_pagar,
	# 	'items': items,
	# 	'orden_all ': orden_all ,
	#	'pago_orden': pago_orden,
	# 	}
	# 	return render(request, "order/invoice.html", context)


#Estadisticas.

# Los Valores de Proveedores, Valores de los Productos, %de Ganacia, % de Credito, Valores en el Tiempo, Amortizacion, 