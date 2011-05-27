# coding: utf-8

from django.db import models

class CompanyOtherRadioPortable(models.Model):
    company = models.ForeignKey('Company')
    radio_portable_brand = models.CharField(max_length = 100, verbose_name='Marca', blank=True, null=True)
    radio_portable_model = models.CharField(max_length = 100, verbose_name='Modelo', blank=True, null=True)
    radio_portable_power = models.IntegerField(max_length = 4, verbose_name='Potencia', blank=True, null=True)
    
    def __unicode__(self):
        return u'%s: %s' % (self.radio_portable_brand, self.radio_portable_model, self.radio_portable_power)

    class Meta:
        ordering = ['id']
        app_label = 'censo'