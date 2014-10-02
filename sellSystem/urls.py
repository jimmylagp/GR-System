from django.conf.urls import patterns, include, url
from .views import Home, Productos

urlpatterns = patterns('',

	url(r'^$', home.as_view(), name="index"),
	url(r'^$productos/', productos.as_view(), name="productos"),

)
