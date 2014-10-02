from django.views.generic import ListView
from django.db.models import F
from sellSystem.models import Producto

# Create your views here.

class Home(ListView):
	template_name = 'home.html'

	queryset = Producto.objects.filter(cantidad__lte=F('reserva'))


class Productos(ListView):
	template_name = 'productos.html'

	queryset = Producto.objects.all()