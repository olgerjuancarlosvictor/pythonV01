from django.shortcuts import render
from django.views.generic import CreateView
from .models import Autor


class RegistrarAutor(CreateView):
	
	template_name = 'autores/registrarAutor.html'
	model = Autor
	fields = ('nombre','apellido','pais','descripcion','foto')

	  #template_name = 'autores/registrarAutor.html'
	  #model = Autor



