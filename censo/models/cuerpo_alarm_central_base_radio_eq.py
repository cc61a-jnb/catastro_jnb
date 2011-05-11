# coding: utf-8

from django.db import models

class CuerpoAlarmCentralBaseRadioEq(models.Model):
    cuerpo = models.ForeignKey('Cuerpo')
    quantity = models.IntegerField(default=0, verbose_name='Cantidad')
    manufacturer = models.CharField(max_length = 100, verbose_name='Marca', blank=True, null=True)
    model = models.CharField(max_length = 100, verbose_name='Modelo', blank=True, null=True)
    power = models.IntegerField(default=0, verbose_name='Potencia (W)')
    
    def __unicode__(self):
        return u'%s: %s' % (self.manufacturer, self.model)

    class Meta:
        ordering = ['id']
        app_label = 'censo'
