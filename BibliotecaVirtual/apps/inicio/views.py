from django.shortcuts import render, render_to_response, RequestContext
from django.views.generic import TemplateView
# Create your views here.
def index_view(request):
	return render_to_response('inicio/index.html', context=RequestContext(request))

class index2(TemplateView):
      template_name = 'inicio/index2.html'