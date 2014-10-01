from django.views.generic import TemplateView
from sellSystem.models import Producto

# Create your views here.

class home(TemplateView):
	template_name = 'home.html'