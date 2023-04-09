from django.db import models

class Obra(models.Model):
    col_comunidad = models.CharField(max_length=200)
    rubro = models.CharField(max_length=60)
    subclasificacion = models.CharField(max_length=40)
    nombre_obra = models.CharField(max_length=200)
    tenencia = models.CharField(max_length=30)
    modalidad_ejecucion = models.CharField(max_length=17)
    metas_cantidad = models.PositiveIntegerField()
    metas_unidad = models.CharField(max_length=10)
    metas_beneficiarios = models.PositiveIntegerField()
    costo_total = models.FloatField()
    inv_estatal = models.FloatField()
    inv_federal = models.FloatField()
    fism= models.FloatField()

    #supervisor=models.ForeignKey(Supervisor)
    #modalidad_adjudicacion=models.ForeignKey(modalidad_adjudicacion)




