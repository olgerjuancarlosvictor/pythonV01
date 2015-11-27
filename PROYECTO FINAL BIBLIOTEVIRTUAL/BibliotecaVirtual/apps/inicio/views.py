from django.views.generic import TemplateView,FormView
from .forms import UserForm
from django.core.urlresolvers import reverse_lazy
from .models import Perfiles


class Registrarse(FormView):
	template_name = 'inicio/registrarse.html'
	form_class = UserForm
	success_url = reverse_lazy('registrarse')

	def form_valid(self, form):
		user = form.save()
		perfil = Perfiles()
		perfil.usuario = user
		perfil.num_tele = form.cleaned_data['num_tele']
		perfil.save()
		return super(Registrarse , self).form_valid(form)

#from django.shortcuts import render, render_to_response, RequestContext

#from django.views.generic import TemplateView

#def index_view(request):
	#return render_to_response('inicio/index.html', context=RequestContext(request))

#class index2(TemplateView):
      #template_name = 'inicio/index2.html'