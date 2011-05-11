# coding: utf-8

from django.db import models

class PortadaCompanyData(models.Model):
    company = models.OneToOneField('Company')
    director_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Director')
    captain_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Capitán')
    secretary_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Secretario')
    tesorero_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Tesorero')
    lieutenant_1_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Teniente 1°')
    lieutenant_2_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Teniente 2°')
    lieutenant_3_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Teniente 3°')
    lieutenant_4_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Teniente 4°')
    assistant_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Ayudante')
    observations = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return unicode(self.company)

    class Meta:
        ordering = ['company']
        app_label = 'censo'
