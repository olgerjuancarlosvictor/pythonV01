from django.conf.urls import patterns, url

from apps.inicio.views import index2

urlpatterns = patterns('apps.inicio.views',
	                   url(r'^$','index_view', name="index"),
	                   
	                   url(r'^index/', index2.as_view()),
                    
	                  )


