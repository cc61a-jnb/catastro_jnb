from django.db import models
from django.contrib.auth.models import User

class Occupation(models.Model):
    name = models.CharField(max_length = 255, default = '')
    
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        app_label = 'censo'
