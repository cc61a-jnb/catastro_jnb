# coding: utf-8

from django.db import models

class PortableRadioEquipment(models.Model):
    minor_material_company = models.ForeignKey('MinorMaterialCompanyData', null=True, blank=True)
    ## Material Mayor Cuerpo (ForeignKey)
    manufacturer = models.CharField(max_length = 100, verbose_name='Marca', null=True, blank=True)
    model = models.CharField(max_length = 100, verbose_name='Modelo', null=True, blank=True)
    power = models.IntegerField(verbose_name='Decíbeles', null=True, blank=True)
    quantity = models.IntegerField(verbose_name='Cantidad', null=True, blank=True)
    
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['manufacturer', 'model']
        app_label = 'censo'
