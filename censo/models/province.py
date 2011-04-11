from django.db import models

class Province(models.Model):
    name = models.CharField(max_length = 100)
    region = models.ForeignKey('Region')
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        app_label = 'censo'