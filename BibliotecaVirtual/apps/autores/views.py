from django.shortcuts import render
from django.views.generic import CreateView, TemplateView,ListView
from .models import Autor
from django.core.urlresolvers import reverse_lazy


class RegistrarAutor(CreateView):
	
	template_name = 'autores/registrarAutor.html'
	model = Autor
	fields = ('nombre','apellido','pais','descripcion','foto')
	success_url = reverse_lazy('reportar_autor')

	  #template_name = 'autores/registrarAutor.html'
	  #model = Autor



class ReportarAutor (ListView):
	template_name = 'autores/reportarAutor.html'
	model = Autor