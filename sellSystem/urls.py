from django.conf.urls import patterns, include, url
from .views import Home, Productos

urlpatterns = patterns('',

	url(r'^$', Home.as_view(), name="home"),
	url(r'^productos/$', Productos.as_view(), name="productos"),

)
