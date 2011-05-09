# coding: utf-8

from django.db import models

class CuerpoServiceActsData(models.Model):
    cuerpo = models.OneToOneField('censo.Cuerpo', blank=True)

    def __unicode__(self):
        return self.cuerpo.name

    class Meta:
        ordering = ['cuerpo']
        app_label = 'censo'


    structural_fire_quantity = models.IntegerField(null=True, blank=True, help_text="TEST HELP", verbose_name='10.0 Fuego Estructural')
    vehicles_fire_quantity = models.IntegerField(null=True, blank=True, verbose_name='10.1 Fuego en Vehiculos')
    outdoors_fire_quantity = models.IntegerField(null=True, blank=True, verbose_name='10.2 Fuego en áreas abiertas')
    rescue_victims_vehicles_quantity = models.IntegerField(null=True, blank=True, verbose_name='10.3 Rescate Vehicular')
    rescue_victims_not_vehicles_quantity = models.IntegerField(null=True, blank=True, verbose_name='10.4 Rescate No vehicular')
    incidents_explosive_materials_quantity = models.IntegerField(null=True, blank=True, verbose_name='10.5 Incidentes con Materiales Peligrosos')
    incidents_combustible_gases_quantity = models.IntegerField(null=True, blank=True, verbose_name='10.6 Incidentes con gases combustibles')
    electrical_emergency_quantity = models.IntegerField(null=True, blank=True, verbose_name='10.7 Emergencia con energía electrica')
    other_emergencies_quantity = models.IntegerField(null=True, blank=True, verbose_name='10.8 Otras emergencias')
    revision_inspection_quantity =models.IntegerField(null=True, blank=True, verbose_name='10.9 Inspección y revisión')
    debris_removal_quantity =models.IntegerField(null=True, blank=True, verbose_name='10.10 Rebrote de fuego o remoción de escombros')
    support_other_cuerpos_quantity =models.IntegerField(null=True, blank=True, verbose_name='10.11 Apoyo a otros cuerpos de bomberos')


    # Observaciones
    observations = models.TextField(null=True, blank=True, verbose_name='')
