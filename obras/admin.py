from django.contrib import admin
from . import models

class ObrasAdmin(admin.ModelAdmin):
	list_display =('col_comunidad','nombre_obra', 'costo_total' )


admin.site.register(models.Obra, ObrasAdmin)
