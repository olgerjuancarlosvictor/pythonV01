from django.conf.urls import patterns, url


urlpatterns = patterns('apps.inicio.views',
	                   url(r'^$','index_view', name="index"),
	                   #url(r'^index/$',index2.as_view(), name="index2"),

	                  )