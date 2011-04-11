from django.db import models

class Region(models.Model):
    name = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        app_label = 'censo'