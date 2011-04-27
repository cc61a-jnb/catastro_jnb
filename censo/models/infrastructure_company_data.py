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
    fk_property_title_type = models.ForeignKey('PropertyTitleType', verbose_name='Título de propiedad', blank=True, null=True)
    #models.CharField(max_length=255, null=True, blank=True, verbose_name='Título de propiedad')
    property_commodatum_end_year = models.IntegerField(null=True, blank=True, verbose_name='Año término comodato')
    
    rol_sii = models.IntegerField(null=True, blank=True, verbose_name='Rol Sii N°')
    
    inscription_fojas = models.IntegerField(null=True, blank=True, verbose_name='Fojas')
    inscription_number = models.IntegerField(null=True, blank=True, verbose_name='Número')
    inscription_year = models.IntegerField(null=True, blank=True, verbose_name='Año')
    inscription_real_estate_registrar = models.CharField(max_length=255, null=True, blank=True, verbose_name='Conservador de Bienes Raíces de')
    inscription_owner_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Propietario (Nombre)')
    
    # Construcción
    
    # Se pueden elegir varios materiales
    building_material_type = models.ManyToManyField('BuildingMaterialType', blank = True, null = True, verbose_name='Tipo de Material')
    building_material_type_other = models.CharField(max_length=255, null=True, blank=True, verbose_name='Otros')
    building_initial_construction_year = models.IntegerField(null=True, blank=True, verbose_name='Año construcción inicial')
    building_initial_construction_legal = models.NullBooleanField(verbose_name='Regularizado')
    building_extension_construction_year = models.IntegerField(null=True, blank=True, verbose_name='Año construcción ampliación')
    building_extension_construction_legal = models.NullBooleanField(verbose_name='Regularizado')
    
    # Superficie
    
    terrain_machine_room_m2 = models.IntegerField(null=True, blank=True, verbose_name='Sala de máquinas (m2)')
    terrain_session_room_m2 = models.IntegerField(null=True, blank=True, verbose_name='Sala de sesiones (m2)')
    
    # Oficinas
    director_office = models.NullBooleanField(verbose_name='Director')
    captain_office = models.NullBooleanField(verbose_name='Capitán')
    lieutenant_office = models.NullBooleanField(verbose_name='Teniente')
    secretary_office = models.NullBooleanField(verbose_name='Secretaria')
    treasurer_office = models.NullBooleanField(verbose_name='Tesorero')
    officers_office = models.NullBooleanField(verbose_name='Oficiales')
    common_offices = models.NullBooleanField(verbose_name='Comunes')
    
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
    
    cafeteria = models.NullBooleanField(verbose_name='Casino')
    kitchen = models.NullBooleanField(verbose_name='Cocina')
    living_room = models.NullBooleanField(verbose_name='Salar de estar')
    barrack_house_bedroom = models.NullBooleanField(verbose_name='Dormitorios')
    barrack_house_kitchen = models.NullBooleanField(verbose_name='Cocina')
    barrack_house_bathroom = models.NullBooleanField(verbose_name='Baños')
    common_bathrooms = models.NullBooleanField(verbose_name='Comunes')
    men_bathroom = models.NullBooleanField(verbose_name='Hombres')
    women_bathroom = models.NullBooleanField(verbose_name='Mujeres')
    storage = models.NullBooleanField(verbose_name='Bodega')
    others = models.CharField(max_length=255, null=True, blank=True, verbose_name='Otros')
    
    # Fotografías requeridas. Al final las fotos SI se suben. Vijay vera esta parte
    
    observations = models.TextField(null=True, blank=True, verbose_name='Observaciones')
