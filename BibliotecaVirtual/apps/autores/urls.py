from django.conf.urls import patterns, url
from .views import RegistrarAutor

urlpatterns = patterns('apps.autores.views',

	                   url(r'^registrar/$', RegistrarAutor.as_view(), name="registrar_autor"),
                    
	                  )



