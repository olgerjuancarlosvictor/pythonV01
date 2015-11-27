from django.contrib import admin
from .models import Autor

# Register your models here.
class autorAdmin(admin.ModelAdmin):
	list_display = ["__unicode__","apellido","pais"]
	class Meta:
		models= Autor
	

admin.site.register(Autor, autorAdmin)
