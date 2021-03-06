from django.conf.urls import patterns, include, url
from .views import Home, Productos, Clientes, Rutas, Proveedores, NuevoPedido, AgregarProductos

urlpatterns = patterns('',

	url(r'^$', Home.as_view(), name="home"),
	url(r'^productos/$', Productos.as_view(), name="productos"),
	url(r'^clientes/$', Clientes.as_view(), name="clientes"),
	url(r'^rutas/$', Rutas.as_view(), name="rutas"),
	url(r'^proveedores/$', Proveedores.as_view(), name="proveedores"),
	url(r'^nuevo-pedido/$', NuevoPedido.as_view(), name="nuevoPedido"),
	url(r'^nuevo-pedido/$', NuevoPedido.as_view(), name="nuevoPedido"),
	url(r'^nuevo-pedido/agregar-productos/$', AgregarProductos.as_view(), name="agregarProductos"),

)