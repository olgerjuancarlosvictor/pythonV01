from django.shortcuts import render, render_to_response,RequestContext

# Create your views here.

#from django.http import HttpResponse


def index_view(request):
    return render_to_response('index.html',context=RequestContext(request))
