# coding: utf-8

from django.db import models

class MinorMaterialCompanyData(models.Model):

    company = models.OneToOneField('censo.Company', blank=True)

    def __unicode__(self):
        return unicode(self.company)

    class Meta:
        ordering = ['company']
        app_label = 'censo'

    # Uniformes normados
    jackets_quantity = models.IntegerField(null=True, blank=True, verbose_name='Chaquetas')
    pants_or_overalls_quantity = models.IntegerField(null=True, blank=True, verbose_name='Pantalones ó jardineras')
    helmets_quantity = models.IntegerField(null=True, blank=True, verbose_name='Cascos')
    gloves_quantity = models.IntegerField(null=True, blank=True, verbose_name='Guantes')
    short_capes_quantity = models.IntegerField(null=True, blank=True, verbose_name='Esclavinas')
    fireman_shoes_company_quantity = models.IntegerField(null=True, blank=True, verbose_name='Botas, bototos ó zapatos de Compañía')
    fireman_shoes_volunteer_quantity = models.IntegerField(null=True, blank=True, verbose_name='Botas, bototos ó zapatos de Voluntarios')

    # Equipamiento ERA
    scott_after_2004_quantity = models.IntegerField(null=True, blank=True, verbose_name='Scott (desde 2004 en adelante)')
    racal_quantity = models.IntegerField(null=True, blank=True, verbose_name='Racal y otros antiguos')
    fensy_quantity = models.IntegerField(null=True, blank=True, verbose_name='Fensy')
    scott_before_2004_quantity = models.IntegerField(null=True, blank=True, verbose_name='Scott antes del 2004')
    mSA_quantity = models.IntegerField(null=True, blank=True, verbose_name='MSA')

    # Equipamiento menor
    hosepipe_38mm_quantity = models.IntegerField(null=True, blank=True, verbose_name='Mangueras de 38mm')
    hosepipe_50mm_quantity = models.IntegerField(null=True, blank=True, verbose_name='Mangueras de 50mm')
    hosepipe_70mm_quantity = models.IntegerField(null=True, blank=True, verbose_name='Mangueras de 70mm')
    hosepipe_forest_quantity = models.IntegerField(null=True, blank=True, verbose_name='Mangueras forestales')

    python_50adjustable_quantity=models.IntegerField(null=True, blank=True, verbose_name='Pitón 50 regulable')
    python_50tube_quantity=models.IntegerField(null=True, blank=True, verbose_name='Pitón 50 de tubo')
    python_70adjustable_quantity=models.IntegerField(null=True, blank=True, verbose_name='Pitón 70 regulable')
    python_70tube_quantity=models.IntegerField(null=True, blank=True, verbose_name='Pitón 70 de tubo')

    tripok_quantity=models.IntegerField(null=True, blank=True, verbose_name='Nº de Trifurcas')
    twins_quantity=models.IntegerField(null=True, blank=True, verbose_name='Nº de Gemelos')
    motorpump_quantity=models.IntegerField(null=True, blank=True, verbose_name='Nº de Motobombas')

    # Compresor de aire
    aircompressor_fixed_quantity=models.IntegerField(null=True, blank=True, verbose_name='Nº de Compresores de Aire Fijo')
    aircompressor_bycar_quantity=models.IntegerField(null=True, blank=True, verbose_name='Nº de Compresores de Aire En Vehiculo')

    # Cascada

    cascade_cylinder_quantity=models.IntegerField(null=True, blank=True, verbose_name='Nº de Cilindros de la Cascada')
    cascade_fixed_quantity=models.IntegerField(null=True, blank=True, verbose_name='Nº de Cascadas Fijo')
    cascade_bycar_quantity=models.IntegerField(null=True, blank=True, verbose_name='Nº de Cascadas En Vehiculo')

    # Iluminación

    electricgenerator_fixed_in_car_quantity=models.IntegerField(null=True, blank=True, verbose_name='Nº de Generadores Electricos Fijos en Carros')
    fk_electricgenerator_fixed_in_car_potency=models.ForeignKey('PotencyRange', null=True, blank=True, verbose_name='Potencia de los Generadores Electricos Fijos en Carros', related_name='+')
    electricgenerator_portable_quantity=models.IntegerField(null=True, blank=True, verbose_name='Nº de Generadores Electricos Portátiles')
    fk_electricgenerator_portable_potency=models.ForeignKey('PotencyRange', null=True, blank=True, verbose_name='Potencia de los Generadores Electricos Portátiles', related_name='+')
    electricgenerator_fixed_in_barracks_quantity=models.IntegerField(null=True, blank=True, verbose_name='Nº de Generadores Electricos Fijos en cuarteles')
    fk_electricgenerator_fixed_in_barracks_potency=models.ForeignKey('PotencyRange', null=True, blank=True, verbose_name='Potencia de los Generadores Electricos Fijos en cuarteles', related_name='+')

    # Equipos de Radio Base
    base_radio_equipment_quantity = models.IntegerField(null=True, blank=True, verbose_name='Cantidad')
    base_radio_equipment_manufacturer = models.CharField(max_length=255, null=True, blank=True, verbose_name='Marca')
    base_radio_equipment_model = models.CharField(max_length=255, null=True, blank=True, verbose_name='Modelo')
    base_radio_equipment_power = models.IntegerField(null=True, blank=True, verbose_name='Potencia (W)')


    # Otros
    airmattresses_quantity=models.IntegerField(null=True, blank=True, verbose_name='Nº de Colchones inflables')
    defibrillator_quantity=models.IntegerField(null=True, blank=True, verbose_name='Nº de Desfribiladores')
    oxygen_equipment_quantity=models.IntegerField(null=True, blank=True, verbose_name='Nº de Equipos para aplicación de oxígeno a pacientes')
    generators_quantity=models.IntegerField(null=True, blank=True, verbose_name='Nº de Grupos electrógenos')
    hydraulic_equipment_quantity=models.IntegerField(null=True, blank=True, verbose_name='Nº de Equipos hidráulicos de extricación')
    chainsaw_quantity=models.IntegerField(null=True, blank=True, verbose_name='Nº de  Motosierras')
    firesfans_quantity=models.IntegerField(null=True, blank=True, verbose_name='Nº de  Ventiladores para incendios')
    containers_proteinconcentrate_quantity=models.IntegerField(null=True, blank=True, verbose_name='Nº de Bidones de concentrado proteínico')
    containers_syntheticconcentrate_quantity=models.IntegerField(null=True, blank=True, verbose_name='Nº de Bidones de concentrado sintético')
    foam_generating_equipment_quantity=models.IntegerField(null=True, blank=True, verbose_name='Nº de Equipos generadores de espuma')
    instruments_for_detection_of_combustible_gases_quantity=models.IntegerField(null=True, blank=True, verbose_name='Nº de Instrumentos de detección de combustibles')
    instruments_of_toxic_gas_analysis_quantity=models.IntegerField(null=True, blank=True, verbose_name='Nº de Instrumentos de análisis de gases tóxicos')
    levelA_chemical_protection_suits_quantity=models.IntegerField(null=True, blank=True, verbose_name='Nº de Trajes protección química Nivel A')
    levelB_chemical_protection_suits_quantity=models.IntegerField(null=True, blank=True, verbose_name='Nº de Trajes protección química Nivel B')
    protective_clothing_coated_aluminized_quantity=models.IntegerField(null=True, blank=True, verbose_name='Nº de Trajes de protección con cubierta aluminizada')
    hazmat_seal_kits_quantity=models.IntegerField(null=True, blank=True, verbose_name='Nº de Kits de sellado Hazmat')

    # Equipos de Radio
    portable_radio_equipment_quantity = models.IntegerField(null=True, blank=True, verbose_name='Cantidad')
    portable_radio_equipment_manufacturer = models.CharField(max_length=255, null=True, blank=True, verbose_name='Marca')
    portable_radio_equipment_model = models.CharField(max_length=255, null=True, blank=True, verbose_name='Modelo')
    
    # Antena
    antenna_equipment_quantity = models.IntegerField(null=True, blank=True, verbose_name='Cantidad')
    antenna_equipment_manufacturer = models.CharField(max_length=255, null=True, blank=True, verbose_name='Marca')
    antenna_equipment_model = models.CharField(max_length=255, null=True, blank=True, verbose_name='Modelo')
    antenna_equipment_power = models.IntegerField(null=True, blank=True, verbose_name='Decibeles')

    # Observaciones
    observations = models.TextField(null=True, blank=True, verbose_name='')