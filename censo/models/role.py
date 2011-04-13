from django.db import models
from django.contrib.auth.models import User

class Role(models.Model):
    old_id = models.IntegerField(unique = True)
    name = models.CharField(max_length = 100, default = '')
    
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        app_label = 'censo'
