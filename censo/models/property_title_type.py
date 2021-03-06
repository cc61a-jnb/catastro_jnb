# coding: utf-8

from django.db import models

class PropertyTitleType(models.Model):
    name = models.CharField(max_length = 100)
    ordering = models.IntegerField(default = 0)
    requires_end_year = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['ordering', 'name']
        app_label = 'censo'
