from django.views.generic import ListView
from django.db.models import F, Q
from sellSystem.models import Producto
from sellSystem.forms import BuscarProducto
import operator

# Create your views here.

class Home(ListView):
	template_name = 'home.html'

	queryset = Producto.objects.filter(cantidad__lte=F('reserva'))


class Productos(ListView):
	template_name = 'productos.html'
	model = 'Producto'
	paginate_by = 5

	#queryset = Producto.objects.all()
	
	def get_queryset(self):
		q = self.request.GET
		nombre = q.get('nombre')
		tipo = q.get('tipo')
		facturado = q.get('facturado')
		q_objects = []

		if nombre is not None or tipo is not None or facturado is not None:
			
			if nombre != u'' or tipo != u'' or facturado != u'':
				if nombre != u'':
					q_objects.append( Q(nombre__icontains=nombre) )
			
				if tipo != u'':
					q_objects.append( Q(tipo=int(tipo)) )
				
				if facturado != u'':
					q_objects.append( Q(facturado=int(facturado)) )

				qset = Producto.objects.filter(reduce(operator.and_, q_objects)).distinct()
			else:
				qset = Producto.objects.all()

		else:
			qset = Producto.objects.all()

		return qset

	def get_context_data(self, **kwargs):
		# Llamamos ala implementacion primero del  context
		context = super(Productos, self).get_context_data(**kwargs)
		# Agregamos el publisher

		q = self.request.GET.copy()
		if q.has_key('page'):
			del q['page']

		context['queries'] = q
		return context