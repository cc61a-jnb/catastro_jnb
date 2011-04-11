# coding: utf-8

from django.db import models

class Cuerpo(models.Model):
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
    
    # De aca para abajo: Cosas pendientes y dudosas
    
    # TODO: logo
    cuer_npers_juri = models.IntegerField(blank=True, null=True) # No estamos seguros de para que es, borrar si no sirve para nada
    company = models.ForeignKey('Company', null=True, related_name='company_cuerpo') # en caso que un cuerpo sea también compañía

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        app_label = 'censo'
