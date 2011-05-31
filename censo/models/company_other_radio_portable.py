# coding: utf-8

from django.db import models

class CompanyOtherRadioPortable(models.Model):
    company = models.ForeignKey('Company')
    radio_portable_quantity = models.IntegerField(max_length = 3, verbose_name='Cantidad', blank=True, null=True)
    fk_radio_portable_brand = models.ForeignKey('PortableBrand', verbose_name='Marca', blank=True, null=True)
    radio_portable_model = models.CharField(max_length = 100, verbose_name='Modelo', blank=True, null=True)
    
    def __unicode__(self):
        return u'%s: %s' % (self.radio_portable_quantity, self.radio_portable_brand, self.radio_portable_model)

    class Meta:
        ordering = ['id']
        app_label = 'censo'
