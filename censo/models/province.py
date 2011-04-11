from django.db import models

class Province(models.Model):
    name = models.CharField(max_length = 100)
    region = models.ForeignKey('Region')
    old_id = models.IntegerField()
    
    def __unicode__(self):
        return self.name + ' (' + unicode(self.region) + ')'

    class Meta:
        ordering = ['name']
        app_label = 'censo'
