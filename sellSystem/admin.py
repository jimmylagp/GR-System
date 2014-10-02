from django.contrib import admin
from django.db.models import F
from .models import *
# Register your models here.

class TipoProducto(admin.SimpleListFilter):
	title = "Tipo"
	parameter_name = "tipo"

	def lookups(self, request, model_admin):
		return (
			(0, "De Bicicleta"),
			(1, "De Motocicleta"),
		)

	def queryset(self, request, queryset):
		if self.value():
			return queryset.filter(tipo=self.value())
		else:
			return queryset

class ReservaProducto(admin.SimpleListFilter):
	title = "Reservas"
	parameter_name = "reservas"

	def lookups(self, request, model_admin):
		return (
			(1, "En reserva"),
		)

	def queryset(self, request, queryset):
			if self.value() == '1':
				return queryset.filter(cantidad=F('reserva'))
			else:
				return queryset

class Facturado(admin.SimpleListFilter):
	title = "Facturables"
	parameter_name = "facturable"

	def lookups(self, request, model_admin):
		return (
			(0, "No Facturados"),
			(1, "Facturados"),
		)

	def queryset(self, request, queryset):
		if self.value():
			return queryset.filter(facturado=self.value())
		else:
			return queryset

class ReadOnlyModelAdmin(admin.ModelAdmin):
	actions = None

	def get_readonly_fields(self, request, obj=None):
		return self.fields or [f.name for f in self.model._meta.fields]

	def has_add_permission(self, request):
		return False

	# Allow viewing objects but not actually changing them
	def has_change_permission(self, request, obj=None):
		if request.method not in ('GET', 'HEAD'):
			return False
		return super(ReadOnlyModelAdmin, self).has_change_permission(request, obj)

	#def has_delete_permission(self, request, obj=None):
	#	return False

class ClienteAdmin(admin.ModelAdmin):
	list_display = ("nombre", "apellidos", "ciudad", "id_ruta")
	list_filter = ("id_ruta",)
	search_fields = ("nombre",)

class ProveedorAdmin(admin.ModelAdmin):
	list_display = ("nombre", "apellidos", "empresa",)
	search_fields = ("nombre",)

class ProductoAdmin(admin.ModelAdmin):
	list_display = ("cantidad", "nombre", "precio", "tipo", "facturado", "anotaciones",)
	list_display_links = ("nombre",)
	list_filter = ("id_proveedor", TipoProducto, ReservaProducto, Facturado,)
	search_fields = ("nombre",)

class PedidoAdmin(ReadOnlyModelAdmin):
	list_display = ("creacion", "descuento", "pagado",)


admin.site.register(Cliente, ClienteAdmin,)
admin.site.register(Proveedor, ProveedorAdmin,)
admin.site.register(Producto, ProductoAdmin,)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Ruta,)