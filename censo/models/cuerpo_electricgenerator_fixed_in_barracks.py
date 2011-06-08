# coding: utf-8

from django.db import models

class CuerpoElectGeneratorFixedBarracks(models.Model):
    infrastructure = models.ForeignKey('CuerpoInfrastructureData')
    quantity = models.IntegerField(verbose_name='Cantidad', null=True, blank=True)
    fk_potency = models.ForeignKey('PotencyRange', verbose_name='Potencia', null=True, blank=True, related_name='+')
    
    def __unicode__(self):
        return u'%s: %s' % (self.quantity, self.potency)

    class Meta:
        ordering = ['id']
        app_label = 'censo'
