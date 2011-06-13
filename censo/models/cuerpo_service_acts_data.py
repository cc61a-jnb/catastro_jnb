# coding: utf-8

from django.db import models

class CuerpoServiceActsData(models.Model):
    cuerpo = models.OneToOneField('censo.Cuerpo', blank=True)

    def __unicode__(self):
        return self.cuerpo.name

    class Meta:
        ordering = ['cuerpo']
        app_label = 'censo'


    structural_fire_quantity = models.IntegerField(null=True, blank=True, help_text="Ej: Casas habitación, oficinas, malls, supermercados, hoteles, hospitales, cárceles, barracas, industrias o bodegas.", verbose_name='a. Fuego Estructural')
    vehicles_fire_quantity = models.IntegerField(null=True, blank=True, help_text="Ej: Autos, camionetas, motocicletas, buses, aeronaves, ferrocarriles o trenes.",  verbose_name='b. Fuego en Vehiculos o medios de transporte')
    outdoors_fire_quantity = models.IntegerField(null=True, blank=True, help_text="Ej: Pastizales, plantaciónes agricolas, parques nacionales, microbasurales, desechos, vertederos o bienes de uso público.", verbose_name='c. Fuego en áreas abiertas')
    rescue_victims_not_vehicles_quantity = models.IntegerField(null=True, blank=True,  help_text="Ej: Ascensores, estructuras colapsadas, minas, rios, mar, aluviones, volcán, cerro o nieve.", verbose_name='d. Rescate No vehicular')
    rescue_victims_vehicles_quantity = models.IntegerField(null=True, blank=True, help_text="Ej: Auto, camión, bus, motocicleta, ferroviario, vehículos de emergencias, maquinarias agricolas.", verbose_name='e. Rescate de víctimas desde vehiculos')
    incidents_explosive_materials_quantity = models.IntegerField(null=True, blank=True, help_text="Ej: Explosivos, gases, líquidos, solidos, comburentes, peróxidos organicos, venenos liquidos o sólidos, radioactivos o corrosivos.",  verbose_name='f. Control de incidentes que involucren materiales peligrosos')
    incidents_combustible_gases_quantity = models.IntegerField(null=True, blank=True, help_text="Ej: Gas licuado, gas natural, gas de cuidad, presencia de monoxido de carbono o explosiones.",  verbose_name='g. Incidentes con gases combustibles')
    electrical_emergency_quantity = models.IntegerField(null=True, blank=True, help_text="Ej: Tendido aéreo de alta y baja tensión, tendido subterráeo de alta y baja tensión, acometida trifásica ó monofásica, medidor de energía.",  verbose_name='h. Emergencia con energía electrica')
    other_emergencies_quantity = models.IntegerField(null=True, blank=True, help_text="Ej: Abrir casa, departamento u oficina, asistencia preventiva, trabajos en alturas, rastreo de personas o recuperación de cadáveres.",  verbose_name='i. Otras servicios de emergencia')
    revision_inspection_quantity =models.IntegerField(null=True, blank=True,  help_text="Ej: Peritajes, revisión de edificios, inspección de local comercial, industrias, grifos o simulacros.", verbose_name='j.Servicios de inspección y revisión')
    debris_removal_quantity =models.IntegerField(null=True, blank=True,  help_text="Ej: Rebrote de fuego de cualquier fuego anterior, en vehículos, en lugar abierto.", verbose_name='k. Rebrote de fuego o remoción de escombros')
    support_other_cuerpos_quantity =models.IntegerField(null=True, blank=True,  help_text="Ej: Apoyo a otros cuerpos en cualquiera de los actos del servicio detallados anteriormente.", verbose_name='m. Apoyo a otros cuerpos de bomberos')


    # Observaciones
    observations = models.TextField(null=True, blank=True, verbose_name='')
    #Internal only
    is_valid = models.NullBooleanField(verbose_name='¿Formulario válido?')
    #Staff only
    is_complete = models.NullBooleanField(verbose_name='¿Formulario completo?')
    is_correct = models.NullBooleanField(verbose_name='¿Formulario correcto?')
