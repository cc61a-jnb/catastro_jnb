# coding: utf-8

from django.db import models

class CuerpoMaterialMayorGeneratorPort(models.Model):
    material_mayor_data = models.ForeignKey('CuerpoMayorMaterialData')
    quantity= models.IntegerField(verbose_name='Cantidad')
    potency = models.ForeignKey('PotencyRange', verbose_name='Potencia')
    
    def __unicode__(self):
        return u'%d generadores de %s' % (self.quantity, unicode(self.potency))

    class Meta:
        ordering = ['id']
        app_label = 'censo'
