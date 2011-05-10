# coding: utf-8

from django.db import models

class Cuerpo(models.Model):
    old_id = models.IntegerField()
    name = models.CharField(max_length=100, default='')
    rut = models.CharField(max_length=10, default='')
    address = models.CharField(max_length=255, default='')
    commune = models.ForeignKey('Commune', related_name='+', blank=True, null=True)
    phone = models.CharField(max_length=100, default='')
    fax = models.CharField(max_length=100, default='')
    postal_box = models.CharField(max_length=100, default='')
    mail = models.EmailField(default='')
    url = models.CharField(max_length=255, default='')
    foundation_date = models.DateField(blank=True, null=True)
    lemma = models.CharField(max_length=255)
    alarm_central_phone = models.CharField(max_length=100)
    communes = models.ManyToManyField('Commune', blank=True, null=True)
    decree_date = models.DateField(blank=True, null=True) # fecha decreto

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

    # TODO: logo cuerpo

    # número personalidad juridica
    cuer_npers_juri = models.IntegerField(blank=True, null=True)
    # In case that cuerpo is also a company
    company = models.ForeignKey('Company', null=True, related_name='company_cuerpo')



    # TODO: associate cuerpo with companies

    def __unicode__(self):
        return u'%d %s' % (self.old_id, self.name)

    class Meta:
        ordering = ['name']
        app_label = 'censo'
