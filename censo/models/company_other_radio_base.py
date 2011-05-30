# coding: utf-8

from django.db import models

class CompanyOtherRadioBase(models.Model):
    company = models.ForeignKey('Company')
    radio_quantity = models.IntegerField(max_length = 4, verbose_name='Cantidad', blank=True, null=True)
    fk_radio_brand = models.ForeignKey('PortableBrand', verbose_name='Marca', blank=True, null=True)
    radio_model = models.CharField(max_length = 100, verbose_name='Modelo', blank=True, null=True)
    radio_power = models.IntegerField(max_length = 4, verbose_name='Potencia', blank=True, null=True)
    
    
    def __unicode__(self):
        return u'%s: %s' % (self.radio_quantity, self.radio_brand, self.radio_model, self.radio_power)

    class Meta:
        ordering = ['id']
        app_label = 'censo'
