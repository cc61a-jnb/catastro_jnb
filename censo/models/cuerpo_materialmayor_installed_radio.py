# coding: utf-8

from django.db import models

class CuerpoMaterialMayorInstalledRadio(models.Model):
    material_mayor_data = models.ForeignKey('CuerpoMayorMaterialData')
    installed_radio_quantity= models.IntegerField(max_length = 4, verbose_name='Cantidad', blank=True, null=True)
    fk_installed_radio_brand = models.ForeignKey('PortableBrand', verbose_name='Marca', blank=True, null=True)
    installed_radio_model = models.CharField(max_length = 100, verbose_name='Modelo', blank=True, null=True)
    installed_radio_potency=models.IntegerField(max_length = 4, verbose_name='Power', blank=True, null=True)
    
    def __unicode__(self):
        return u'%s: %s' % (unicode(self.fk_installed_radio_brand), self.installed_radio_model)

    class Meta:
        ordering = ['id']
        app_label = 'censo'
