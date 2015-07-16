
from django.conf.urls import patterns,url


#avilitar el administrador django

urlpatterns = patterns ('inicio.views',
    
    #url(r'^$', 'apps.inicio.views.index'),
    url(r'^$', 'index_view', name="index"),
 
)
