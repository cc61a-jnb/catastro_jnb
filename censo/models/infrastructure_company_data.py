# coding: utf-8

from django.db import models

class InfrastructureCompanyData(models.Model):

    company = models.OneToOneField('censo.Company', blank=True)

    def __unicode__(self):
        return self.company.name

    class Meta:
        ordering = ['company']
        app_label = 'censo'
        
    # Terreno
    built_area_front_m2 = models.IntegerField(null=True, blank=True, verbose_name='Superficie Frente (m2)')
    built_area_back_m2 = models.IntegerField(null=True, blank=True, verbose_name='Superficie Fondo (m2)')
    built_area_total_m2 = models.IntegerField(null=True, blank=True, verbose_name='Superficie Total (m2)')
    
    main_street_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Calle Principal')
    secondary_street_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Calle Secundaria')
    narrow_street_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Pasaje')
    
    # Use ChoiceField in form!
    property_title_type = models.CharField(max_length=255, null=True, blank=True, verbose_name='Título de propiedad')
    property_commodatum_end_year = models.IntegerField(null=True, blank=True, verbose_name='Año término comodato')
    
    rol_sii = models.IntegerField(null=True, blank=True, verbose_name='Rol Sii N°')
    
    inscription_fojas = models.IntegerField(null=True, blank=True, verbose_name='Fojas')
    inscription_number = models.IntegerField(null=True, blank=True, verbose_name='Número')
    inscription_year = models.IntegerField(null=True, blank=True, verbose_name='Año')
    inscription_real_estate_registrar = models.CharField(max_length=255, null=True, blank=True, verbose_name='Conservador de Bienes Raíces de')
    inscription_owner_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Propietario (Nombre)')
    
    # Construcción
    
    # Use ChoiceField in form!
    building_material_type = models.CharField(max_length=255, null=True, blank=True, verbose_name='Tipo de material') # Falta validar si se pueden elegir varios (en cuyo caso habría que hacer algo como lo de las especialidades
    building_initial_construction_year = models.IntegerField(null=True, blank=True, verbose_name='Año construcción inicial')
    building_initial_construction_legal = models.NullBooleanField(verbose_name='Regularizado')
    building_extension_construction_year = models.IntegerField(null=True, blank=True, verbose_name='Año construcción ampliación')
    building_extension_construction_legal = models.NullBooleanField(verbose_name='Regularizado')
    
    # Superficie
    
    terrain_machine_room_m2 = models.IntegerField(null=True, blank=True, verbose_name='Sala de máquinas')
    terrain_session_room_m2 = models.IntegerField(null=True, blank=True, verbose_name='Sala de sesiones')
    
    ##TODO: Oficinas
    
    night_guard_office_men_beds = models.IntegerField(null=True, blank=True, verbose_name='N° de camas (Hombres)')
    night_guard_office_men_bathroom = models.IntegerField(null=True, blank=True, verbose_name='N° de baños (Hombres)')
    night_guard_office_men_bathroom_showers = models.IntegerField(null=True, blank=True, verbose_name='N° de Duchas')
    night_guard_office_men_bathroom_wc = models.IntegerField(null=True, blank=True, verbose_name='N° de WC')
    night_guard_office_men_bathroom_urinary = models.IntegerField(null=True, blank=True, verbose_name='N° de Urinarios')
    night_guard_office_women_beds = models.IntegerField(null=True, blank=True, verbose_name='N° de camas (Mujeres)')
    night_guard_office_women_bathroom = models.IntegerField(null=True, blank=True, verbose_name='N° de baños (Mujeres)')
    night_guard_office_women_bathroom_showers = models.IntegerField(null=True, blank=True, verbose_name='N° de Duchas')
    night_guard_office_women_bathroom_wc = models.IntegerField(null=True, blank=True, verbose_name='N° de WC')
    night_guard_office_kitchen = models.NullBooleanField(verbose_name='Cocina de la Guardia')
    
    ##TODO: El resto
    
    observations = models.TextField(null=True, blank=True, verbose_name='')
