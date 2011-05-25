# coding: utf-8

from django.db import models

class CompanyOtherRadioBase(models.Model):
    company = models.ForeignKey('Company')
    radio_brand = models.CharField(max_length = 100, verbose_name='Marca', blank=True, null=True)
    radio_model = models.CharField(max_length = 100, verbose_name='Modelo', blank=True, null=True)
    
    def __unicode__(self):
        return u'%s: %s' % (self.radio_brand, self.radio_model)

    class Meta:
        ordering = ['id']
        app_label = 'censo'