from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
	url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATICFILES_DIRS}),
	url(r'^', include('sellSystem.urls')),
)
