# coding: utf-8

from django.db import models
from sorl.thumbnail import ImageField

class CuerpoInfrastructureData(models.Model):

    cuerpo = models.OneToOneField('censo.Cuerpo', blank=True)

    def __unicode__(self):
        return self.cuerpo.name

    class Meta:
        ordering = ['cuerpo']
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
    property_commodatum_end_year = models.IntegerField(null=True, blank=True, verbose_name='Año término comodato o arriendo')

    rol_sii = models.IntegerField(null=True, blank=True, verbose_name='Rol Avaluo fiscal N° (SII)')
    # Datos de Inscripción conservador
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
    supervisor_office = models.NullBooleanField(verbose_name='Oficina del Superintendente')
    major_office = models.NullBooleanField(verbose_name='Oficina del Comandante')
    general_secretary_office = models.NullBooleanField(verbose_name='Oficina del Secretaria(o) General')
    general_treasurer_office = models.NullBooleanField(verbose_name='Oficina de Tesorero General')

    #Otras oficinas
    #Dinamico?

    #Dependencias

    cafeteria = models.NullBooleanField(verbose_name='Casino')
    kitchen = models.NullBooleanField(verbose_name='Cocina')
    living_room = models.NullBooleanField(verbose_name='Salar de estar')
    bathrooms = models.NullBooleanField(verbose_name='Baños')

    #Otras areas
    barrack_house = models.NullBooleanField(verbose_name='Casa cuartelero')
    storage = models.NullBooleanField(verbose_name='Bodega')
    others = models.CharField(max_length=255, null=True, blank=True, verbose_name='Otros')

    # Fotografías requeridas. Al final las fotos SI se suben. Vijay vera esta parte
    # Copy + paste :D
    picture_general_view = ImageField(upload_to = 'cuerpo_pics', blank=True, null=True, verbose_name='Vista general')
    picture_front_view = ImageField(upload_to = 'cuerpo_pics', blank=True, null=True, verbose_name='Fachada')
    picture_back_view = ImageField(upload_to = 'cuerpo_pics', blank=True, null=True, verbose_name='Parte posterior')
    picture_machine_room_view = ImageField(upload_to = 'cuerpo_pics', blank=True, null=True, verbose_name=u'Sala de máquinas')
    picture_office_view = ImageField(upload_to = 'cuerpo_pics', blank=True, null=True, verbose_name='Oficinas')
    picture_internal_distribution_view = ImageField(upload_to = 'cuerpo_pics', blank=True, null=True, verbose_name=u'Distribución interior')
    
    # Estado infrastructura
    fk_infrastructure_status = models.ForeignKey('InfrastructureStatus', verbose_name='Estado infrastructura', null=True, blank=True)

   #Observaciones
    observations = models.TextField(null=True, blank=True, verbose_name='')
    
    #Internal only
    is_valid = models.NullBooleanField(verbose_name='¿Formulario válido?')
    #Staff only
    is_complete = models.NullBooleanField(verbose_name='¿Formulario completo?')
    is_correct = models.NullBooleanField(verbose_name='¿Formulario correcto?')
