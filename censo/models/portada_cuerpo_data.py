# coding: utf-8

from django.db import models

class PortadaCuerpoData(models.Model):
    
    cuerpo = models.OneToOneField('censo.Cuerpo', blank=True)
    
    # observaciones  
    observations = models.TextField(null=True, blank=True, verbose_name='')
    
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['observations']
        app_label = 'censo'
