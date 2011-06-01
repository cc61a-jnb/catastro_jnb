# coding: utf-8

from django.db import models

class MotorType(models.Model):
    name = models.CharField(max_length = 255)
    ordering = models.IntegerField(default = 0)
    
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['ordering', 'name']
        app_label = 'censo'
