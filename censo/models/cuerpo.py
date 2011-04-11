from django.db import models

class Cuerpo(models.Model):
    name = models.CharField(max_length = 100, default = '')
    rut = models.CharField(max_length = 10, default = '')
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        app_label = 'censo'