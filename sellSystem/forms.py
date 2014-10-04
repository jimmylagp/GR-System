from django import forms
from sellSystem.models import Producto

class BuscarProducto (forms.Form):
	nombre = forms.CharField(required=False)
	tipo = forms.ChoiceField(required=False)
	facturado = forms.ChoiceField(required=False)

	class Meta:
		model = Producto
		fileds = ('nombre', 'tipo', 'facturado',)