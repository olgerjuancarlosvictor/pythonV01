from django.db import models


class Autor(models.Model):
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	pais = models.CharField(max_length=50)
	descripcion = models.TextField(max_length=200)
	foto = models.ImageField(upload_to='foto_autor')
	#time = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __unicode__(self):
	    return self.nombre
	    #return str(self.time)
	    #return self.apellido
# Create your models here.
