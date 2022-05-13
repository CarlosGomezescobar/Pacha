"""
  TERMS OF USE - 

  Open Source 
 
 Copyright © 2022 Carlos M. Gómez Escobar
"""


from django import forms
from django.db import models
from core.models import *

PAYMENT_CHOICES = (
    ('PG', 'Pago Movil'),
    ('E', 'Efectivo'),
    ('M', 'Metamask'),
    ('P', 'PayPal')
)
CATEGORY_CHOICES = (
    ('Ferreteria', 'Ferreteria'),
    ('Alimentos', 'Alimentos'),
    ('Salud', 'Salud'),
    ('Tendencia', 'Tendencia'),
    ('Otros', 'Otros')
)

#PagoForms / (DONE)

class PagoForm(forms.ModelForm):
    PAYMENT_CHOICES = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices=PAYMENT_CHOICES,)
        
#Cliente Forms / (DONE)

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class SearchClienteForm(forms.ModelForm):
    export_to_CSV = forms.BooleanField(required=False)
    class Meta:
        model = Cliente
        fields =['ci']

class UpdateClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'





#Proveedores Forms / (DONE)

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields ='__all__' 

class SearchProveedorForm(forms.ModelForm):
    export_to_CSV = forms.BooleanField(required=False)
    class Meta:
        model = Proveedor
        fields = ['razon_social']

class UpdateProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields ='__all__'



class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields ='__all__' 

class SearchProductoForm(forms.ModelForm):
    export_to_CSV = forms.BooleanField(required=False)
    class Meta:
        model = Producto
        fields =['titulo']

class UpdateProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields ='__all__'



#ITEM Forms (ITEM) / (DONE)


class ItemSearchForm(forms.ModelForm):
    export_to_CSV = forms.BooleanField(required=False)
    class Meta:
        model = Item
        fields = '__all__' 

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'       

class ItemUpdapteForm(forms.ModelForm):
    class Meta:
        model = Item
        fields ='__all__'



#Stock Forms / (DONE)

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields ='__all__'

class StockSearchForm(forms.ModelForm):
    export_to_CSV = forms.BooleanField(required=False)
    class Meta:
        model = Stock
        fields = '__all__' 

class StockUpdapteForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields ='__all__'
    



#Ordenes de Servicio Forms / 

    #Orden Item
class OrdenItemForm(forms.ModelForm):
    class Meta:
        model = OrdenItem
        fields ='__all__'

class  OrdenItemSearchForm(forms.Form):
    export_to_CSV = forms.BooleanField(required=False)
    class Meta:
        model = OrdenItem
        fields ='__all__'

class OrdenItemUpdapteForm(forms.ModelForm):
    class Meta:
        model = OrdenItem
        fields ='__all__'

    #Order

class OrdenForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields ='__all__'

class OrdenUpdapteForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields ='__all__'

class  OrdenSearchForm(forms.ModelForm):
    export_to_CSV = forms.BooleanField(required=False)
    class Meta:
        model = Orden
        fields ='__all__'



    
    #Invoice

    #