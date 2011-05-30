# coding: utf-8

from django.db import models

class CompanyAntenas(models.Model):
    company = models.ForeignKey('Company')
    antennas_quantity = models.IntegerField(max_length = 4, verbose_name='Cantidad', blank=True, null=True)
    antennas_manufacturer = models.CharField(max_length=255, null=True, blank=True, verbose_name='Marca')
    antennas_model = models.CharField(max_length=255, null=True, blank=True, verbose_name='Modelo')
    antennas_power = models.IntegerField(null=True, blank=True, verbose_name='Decibeles')
    
    
    def __unicode__(self):
        return u'%s: %s' % (self.antenas_quantity, self.antenna_manufacturer, self.antenna_model, self.antenna_power)

    class Meta:
        ordering = ['id']
        app_label = 'censo'