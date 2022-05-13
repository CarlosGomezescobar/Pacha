"""
  TERMS OF USE - 

  Open Source 
 
 Copyright © 2022 Carlos M. Gómez Escobar
"""
from django.urls import path
from django.contrib import admin
from . import views
# Index, Home, List_Items, add_items, delete, stock_detail, update_items, list_proveedores, add_proveedores, delete_proveedores, update_proveedor, list_cliente, add_cliente, delete_cliente, update_cliente, list_order, add_order, delete_order 

from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
#from Finance.views import *
app_name = 'core'


urlpatterns = [
    # path('about/', views.About, name='about),
    # path('servicios/', views.servicios, name='servicios),


    path('', views.Index, name='index'),
    path('logout/', LogoutView.as_view()),
    path('home/', views.Home, name='home'),    
    path('list_Items/', views.List_Items, name='list_Items'),
    path('add_items/', views.add_items, name='add_items'),
    path('delete_items/<str:pk>', views.delete_items, name='delete_items'),
    path('stock_detail/', views.stock_detail, name='stock_detail'),
    path('update_items/<str:pk>', views.update_items, name='update_items'),

    # path('issue_items/<str:pk>', views.issue_items, name='issue_items'),
    # path('issue_items/<str:pk>', views.issue_items, name='issue_items'),
    # path('receive_items/<str:pk>', views.receive_items, name='receive_items'),
    # path('reorder_level/<str:pk>', views.reorder_level, name='reorder_level'),

     #Productos
    path('list_productos/', views.list_productos, name='list_productos'),
    path('add_productos/', views.add_productos, name='add_productos'),
    path('delete_productos/<str:pk>', views.delete_productos, name='delete_productos'),
    path('update_productos/<str:pk>', views.update_productos, name='update_productos'),

    
    #Proveedores

    path('list_proveedores/', views.list_proveedores, name='list_proveedores'),
    path('add_proveedores/', views.add_proveedores, name='add_proveedores'),
    path('delete_proveedores/<str:pk>', views.delete_proveedores, name='delete_proveedores'),
    path('update_proveedores/<str:pk>', views.update_proveedores, name='update_proveedores'),
    #path('orden_proveedores/', views.orden_proveedores, name='orden_proveedores'),
    path('list_invoice/', views.list_invoice, name='list_invoice'),
    path('invoice_stock/', views.invoice_stock, name='invoice_stock'),
    

    #Cliente
    path('list_clientes/', views.list_clientes, name='list_clientes'),
    path('add_clientes/', views.add_clientes, name='add_clientes'),
    path('delete_clientes/<str:pk>', views.delete_clientes, name='delete_clientes'),
    path('update_clientes/<str:pk>', views.update_clientes, name='update_clientes'),


    #Orden de los Servicios (Factura, Orden, Item Orden)
    path('list_order/', views.list_order, name='list_order'),
    path('add_order/', views.add_order, name='add_order'),
    path('delete_order/<str:pk>', views.delete_order, name='delete_order'),



        #path('invoice/', views.invoice, name='invoice'),


        #Payment

        #Otros (About, Contact, Aviso Legas, Politicas Legales)

        #Estadisticas
        
] 	

