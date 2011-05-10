# coding: utf-8

from django.db import models

class PortadaCompanyData(models.Model):

    company = models.OneToOneField('censo.Company', blank=True)
    #oficiales   
    director_name = models.CharField(max_length=255, default = '', verbose_name='Director', blank=True, null=True)
    captain_name = models.CharField(max_length=255, default = '', verbose_name='Capitán', blank=True, null=True)
    secretary_name = models.CharField(max_length=255, default = '', verbose_name='Secretario', blank=True, null=True)
    tesorero_name = models.CharField(max_length=255, default = '', verbose_name='Tesorero', blank=True, null=True)
    lieutenant_1_name = models.CharField(max_length=255, default = '', verbose_name='Teniente 1°', blank=True, null=True)
    lieutenant_2_name = models.CharField(max_length=255, default = '', verbose_name='Teniente 2°', blank=True, null=True)
    lieutenant_3_name = models.CharField(max_length=255, default = '', verbose_name='Teniente 3°', blank=True, null=True)
    lieutenant_4_name = models.CharField(max_length=255, default = '', verbose_name='Teniente 4°', blank=True, null=True)
    assistant_name = models.CharField(max_length=255, default = '', verbose_name='Ayudante', blank=True, null=True)
    
    # observaciones
    observations = models.TextField(null=True, blank=True, verbose_name='')

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['observations']
        app_label = 'censo'
