from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Company(models.Model):
    name = models.CharField(max_length = 100, default = '')
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        app_label = 'censo'
