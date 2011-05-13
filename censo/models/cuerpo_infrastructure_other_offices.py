# coding: utf-8

from django.db import models

class CuerpoInfrastructureOtherOffices(models.Model):
    cuerpo = models.ForeignKey('Cuerpo')
    role_name = models.CharField(max_length = 100, verbose_name='Nombre de cargo', blank=True, null=True)
    
    def __unicode__(self):
        return u'%s :' % (self.role_name)

    class Meta:
        ordering = ['id']
        app_label = 'censo'
