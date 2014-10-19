from django import forms
from sellSystem.models import Producto, Ruta, Cliente

class SeleccionRutaForm (forms.Form):
	ruta = forms.ModelChoiceField(queryset=Ruta.objects.all(), required=True)

class NuevoPedidoForm (forms.Form):
	cliente = forms.ModelChoiceField(queryset=Cliente.objects.all(), required=True)
	descuento = forms.IntegerField(required=True,)