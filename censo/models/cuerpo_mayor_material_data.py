# coding: utf-8

from django.db import models

class CuerpoMayorMaterialData(models.Model):
    cuerpo = models.OneToOneField('censo.Cuerpo', blank=True)

    def __unicode__(self):
        return self.cuerpo.name

    class Meta:
        ordering = ['cuerpo']
        app_label = 'censo'
        
    # informacion del vehiculo
     
    fk_vehicle_type = models.ForeignKey('VehicleType', verbose_name='Tipo de Vehículo', blank=True, null=True)
    denomination = models.CharField(max_length=255, null=True, blank=True, verbose_name='Otros')
    
    
