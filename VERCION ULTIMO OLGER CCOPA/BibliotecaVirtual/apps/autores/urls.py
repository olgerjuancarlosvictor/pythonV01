from django.conf.urls import patterns, url
from .views import RegistrarAutor, ReportarAutor

urlpatterns = patterns('apps.autores.views',

	                   url(r'^registrar/$', RegistrarAutor.as_view(), name="registrar_autor"),
	                   url(r'^reportar/$', ReportarAutor.as_view(), name="reportar_autor"),
                    
	                  )



