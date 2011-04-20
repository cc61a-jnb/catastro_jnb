# coding: utf-8

from django.db import models

class Company(models.Model):
    old_id = models.IntegerField()
    number = models.IntegerField()
    name = models.CharField(max_length = 255, default = '')
    cuerpo = models.ForeignKey('Cuerpo', related_name='cuerpo_company')
    phone = models.CharField(max_length=255, default = '', verbose_name='teléfono')
    mail = models.EmailField(max_length=255, default = '')
    address = models.CharField(max_length=255, default = '', verbose_name='dirección')
    commune = models.ForeignKey('Commune', related_name='+', blank=True, null=True)
    fax = models.CharField(max_length=255, default = '')
    postal_box = models.CharField(max_length=255, default = '')
    website = models.CharField(max_length=255, default = '')
    alarm_central = models.CharField(max_length=255, default = '')
    lemma = models.CharField(max_length=255, default = '')
    specialities = models.ManyToManyField('Speciality', blank = True, null = True)
    communes = models.ManyToManyField('Commune', blank=True, null=True)
    foundation_date = models.DateField(blank = True, null = True, verbose_name='fecha fundación')
    
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        app_label = 'censo'
