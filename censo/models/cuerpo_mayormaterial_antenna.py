# coding: utf-8

from django.db import models

class CuerpoMaterialMayorAntenna(models.Model):
    material_mayor_data = models.ForeignKey('CuerpoMayorMaterialData')
    antenna_quantity= models.IntegerField(max_length = 4, verbose_name='Cantidad', blank=True, null=True)
    antenna_brand = models.CharField(max_length = 100, verbose_name='Marca', blank=True, null=True)
    antenna_model = models.CharField(max_length = 100, verbose_name='Modelo', blank=True, null=True)
    antenna_decibel=models.IntegerField(max_length = 4, verbose_name='Decibeles', blank=True, null=True)
    
    def __unicode__(self):
        return u'%s: %s' % (self.antenna_brand, self.antenna_model)

    class Meta:
        ordering = ['id']
        app_label = 'censo'
