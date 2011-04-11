# coding: utf-8

from django.db import models

class Region(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length = 100)
    capital = models.ForeignKey('Commune', blank = True, null = True)
    
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        app_label = 'censo'
