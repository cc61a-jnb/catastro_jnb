from django.db import models
from django.contrib.auth.models import User

class Occupation(models.Model):
    name = models.CharField(max_length = 100, default = '')
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        app_label = 'censo'
