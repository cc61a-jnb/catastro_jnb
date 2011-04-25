from django.db import models

class Commune(models.Model):
    name = models.CharField(max_length = 100)
    url = models.CharField(max_length = 100) # URL?
    province = models.ForeignKey('Province')
    
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        app_label = 'censo'
