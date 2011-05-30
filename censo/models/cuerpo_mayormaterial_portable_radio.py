# coding: utf-8

from django.db import models

class CuerpoMaterialMayorPortableRadio(models.Model):
    material_mayor_data = models.ForeignKey('CuerpoMayorMaterialData')
    portable_radio_quantity= models.IntegerField(max_length = 4, verbose_name='Cantidad', blank=True, null=True)
    portable_radio_brand = models.CharField(max_length = 100, verbose_name='Marca', blank=True, null=True)
    portable_radio_model = models.CharField(max_length = 100, verbose_name='Modelo', blank=True, null=True)
    
    def __unicode__(self):
        return u'%s: %s' % (self.portable_radio_brand, self.portable_radio_model)

    class Meta:
        ordering = ['id']
        app_label = 'censo'
