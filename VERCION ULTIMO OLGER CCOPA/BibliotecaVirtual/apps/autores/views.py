from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from .models import Autor
from django.core.urlresolvers import reverse_lazy


class RegistrarAutor(CreateView):
	
	template_name = 'autores/registrarAutor.html'
	model = Autor
	fields = ('nombre','apellido','pais','descripcion','foto')
	success_url = reverse_lazy('reportar_autor')

	  #template_name = 'autores/registrarAutor.html'
	  #model = Autor



class ReportarAutor (TemplateView):
	template_name = 'autores/reportarAutor.html'