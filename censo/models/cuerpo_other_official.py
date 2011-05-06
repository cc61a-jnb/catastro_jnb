# coding: utf-8

from django.db import models

class CuerpoOtherOfficial(models.Model):
    cuerpo = models.ForeignKey('Cuerpo')
    role_name = models.CharField(max_length = 100, verbose_name='Cargo')
    person_name = models.CharField(max_length = 100, verbose_name='Nombre')

    def __unicode__(self):
        return u'%s: %s' % (self.person_name, self.role_name)

    class Meta:
        ordering = ['id']
        app_label = 'censo'
