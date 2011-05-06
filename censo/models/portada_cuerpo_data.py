# coding: utf-8

from django.db import models

class PortadaCuerpoData(models.Model):

    cuerpo = models.OneToOneField('censo.Cuerpo', blank=True)
     #oficiales
    superintendent_name = models.CharField(max_length=255, default = '', verbose_name='Superintendente', blank=True, null=True)
    vice_superintendent_name = models.CharField(max_length=255, default = '', verbose_name='Vice  Superintendente', blank=True, null=True)
    commander_name = models.CharField(max_length=255, default = '', verbose_name='Comandante', blank=True, null=True)
    second_commander_name = models.CharField(max_length=255, default = '', verbose_name='Segundo Comandante', blank=True, null=True)
    third_commander_name = models.CharField(max_length=255, default = '', verbose_name='Tercer Comandante', blank=True, null=True)
    forth_commander_name = models.CharField(max_length=255, default = '', verbose_name='Cuarto Comandante', blank=True, null=True)
    secretary_name = models.CharField(max_length=255, default = '', verbose_name='Secretaria General', blank=True, null=True)
    treasury_name = models.CharField(max_length=255, default = '', verbose_name='Tesoreria General', blank=True, null=True)
    intendent_name = models.CharField(max_length=255, default = '', verbose_name='Intendente', blank=True, null=True)
    # observaciones
    observations = models.TextField(null=True, blank=True, verbose_name='')

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['observations']
        app_label = 'censo'
