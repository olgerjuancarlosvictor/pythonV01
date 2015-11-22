from django.db import models
from django.contrib.auth.models import User

class Perfiles(models.Model):
	usuario = models.OneToOneField(User)
	#telefono = models.IntegerField()
	num_tele = models.IntegerField()

	def __unicode__(self):
		return self.usuario.username