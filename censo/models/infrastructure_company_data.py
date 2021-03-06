# coding: utf-8
from django.db import models
from sorl.thumbnail import ImageField

class InfrastructureCompanyData(models.Model):
    company = models.OneToOneField('censo.Company', blank=True)

    def __unicode__(self):
        return unicode(self.company)

    class Meta:
        ordering = ['company']
        app_label = 'censo'
        
    # Terreno
    built_area_surface_m2 = models.IntegerField(null=True, blank=True, verbose_name='Superficie (m2)')
    built_area_front_m2 = models.IntegerField(null=True, blank=True, verbose_name='Frente (m)')
    built_area_back_m2 = models.IntegerField(null=True, blank=True, verbose_name='Fondo (m)')
    built_area_total_m2 = models.IntegerField(null=True, blank=True, verbose_name='Area construida (m2)')
    
    main_street_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Calle Principal')
    secondary_street_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Calle Secundaria')
    narrow_street_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Pasaje')
    
    # Use ChoiceField in form!
    fk_property_title_type = models.ForeignKey('PropertyTitleType', verbose_name='Título de propiedad', null=True, blank=False)
    #models.CharField(max_length=255, null=True, blank=True, verbose_name='Título de propiedad')
    property_rental_commodatum_end_year = models.IntegerField(null=True, blank=True, verbose_name='Año término arriendo o comodato')
    
    rol_sii = models.IntegerField(null=True, blank=True, verbose_name='Rol Avaluo fiscal N° (SII)')
    
    inscription_fojas = models.IntegerField(null=True, blank=True, verbose_name='Fojas')
    inscription_number = models.IntegerField(null=True, blank=True, verbose_name='Número')
    inscription_year = models.IntegerField(null=True, blank=True, verbose_name='Año')
    inscription_real_estate_registrar = models.CharField(max_length=255, null=True, blank=True, verbose_name='Conservador de Bienes Raíces de')
    inscription_owner_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Propietario (Nombre)')
    
    # Construcción
    
    # Se pueden elegir varios materiales
    building_material_type = models.ManyToManyField('BuildingMaterialType', blank = True, null = True, verbose_name='Tipo de Material')
    building_initial_construction_year = models.IntegerField(null=True, blank=True, verbose_name='Año construcción inicial')
    building_initial_construction_legal = models.NullBooleanField(verbose_name='Construcción inicial regularizada')
    building_extension_construction_year = models.IntegerField(null=True, blank=True, verbose_name='Año construcción ampliación')
    building_extension_construction_legal = models.NullBooleanField(verbose_name='Construcción ampliación regularizada')
    
    # Distribución (Ex seccion Superficie)
    
    terrain_machine_room_m2 = models.IntegerField(null=True, blank=True, verbose_name='Sala de máquinas (m2)')
    terrain_session_room_m2 = models.NullBooleanField(verbose_name='Sala de sesiones')
    
    # Oficinas
    director_office = models.NullBooleanField(verbose_name='Oficina de Director')
    captain_office = models.NullBooleanField(verbose_name='Oficina de Capitán')
    lieutenant_office = models.NullBooleanField(verbose_name='Oficina de Teniente')
    secretary_office = models.NullBooleanField(verbose_name='Oficina de Secretaria(o)')
    treasurer_office = models.NullBooleanField(verbose_name='Oficina de Tesorero')
    officers_office = models.NullBooleanField(verbose_name='Oficina de Oficiales')
    common_offices = models.NullBooleanField(verbose_name='Oficinas Comunes')
    
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
    
        # Generadores Eléctricos Fijos en Cuartel

        # campo dinamico
    
    # Fotografías requeridas. Al final las fotos SI se suben. Vijay vera esta parte
    # Vijay haciendo esa parte 
    picture_general_view = ImageField(upload_to = 'company_pics', verbose_name='Vista general', blank=True, null=True)
    picture_front_view = ImageField(upload_to = 'company_pics', verbose_name='Fachada', blank=True, null=True)
    picture_back_view = ImageField(upload_to = 'company_pics', verbose_name='Parte posterior', blank=True, null=True)
    picture_machine_room_view = ImageField(upload_to = 'company_pics', verbose_name=u'Sala de máquinas', blank=True, null=True)
    picture_office_view = ImageField(upload_to = 'company_pics', verbose_name='Oficinas', blank=True, null=True)
    picture_internal_distribution_view = ImageField(upload_to = 'company_pics', verbose_name=u'Distribución interior', blank=True, null=True)
    # Vijay termino esa parte 
    
    # Estado infrastructura
    fk_infrastructure_status = models.ForeignKey('InfrastructureStatus', verbose_name='Estado infrastructura', null=True, blank=True)
    
    observations = models.TextField(null=True, blank=True, verbose_name='')
    
    #Internal only
    is_valid = models.NullBooleanField(verbose_name='¿Formulario válido?')
    #Staff only
    is_complete = models.NullBooleanField(verbose_name='¿Formulario completo?')
    is_correct = models.NullBooleanField(verbose_name='¿Formulario correcto?')
