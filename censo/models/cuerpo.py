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
    
    # TODO: logo cuerpo
    
    # TODO: Not sure what this is
    cuer_npers_juri = models.IntegerField(blank=True, null=True)
    # In case that cuerpo is also a company
    company = models.ForeignKey('Company', null=True, related_name='company_cuerpo')

    # TODO: associate cuerpo with companies

    def __unicode__(self):
        return u'%d %s' % (self.old_id, self.name)

    class Meta:
        ordering = ['name']
        app_label = 'censo'
