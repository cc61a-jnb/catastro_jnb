from django.db import models

class Company(models.Model):
    name = models.CharField(max_length = 100, default = '')
    rut = models.CharField(max_length = 10, default = '')
    region = models.ForeignKey('Region')
    cuerpo = models.ForeignKey('Cuerpo', related_name='cuerpo_company')
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        app_label = 'censo'
