from django.views.generic import TemplateView
from sellSystem.models import Producto

# Create your views here.

class index(TemplateView):
	template_name = 'index.html'