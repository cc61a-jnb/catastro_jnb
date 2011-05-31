# coding: utf-8

from django.db import models
from sorl.thumbnail import ImageField

class CuerpoMayorMaterialData(models.Model):
    cuerpo = models.ForeignKey('censo.Cuerpo')
    company = models.ForeignKey('censo.Company', null=True, blank=True, verbose_name='Compañia')

    def __unicode__(self):
        return unicode(self.company) if self.company else unicode(self.cuerpo)

    class Meta:
        get_latest_by = 'id'
        ordering = ['cuerpo', 'id']
        app_label = 'censo'
        
    
    cuerpo_vehicle_own = models.IntegerField(choices=((0,"------"),(1, u"Superintendencia"), (2,u"Comandancia")), default=0, verbose_name='Nivel Central')
    
    # Informacion del vehiculo
     
    fk_vehicle_type = models.ForeignKey('VehicleType', verbose_name='Tipo de Vehículo', blank=True, null=True)
    denomination = models.CharField(max_length=255, null=True, blank=True, verbose_name='Denominación')
    # Alternativas: Renault, Ford, Chevrolet. Volkwagen, Iveco, Mercedes Benz, Spartan, HME u otro (agregar texto en otro)
    fk_chassis_or_truck_manufacturer = models.ForeignKey('VehicleChassisManufacturer', verbose_name='Marca Chassis/Camión', blank=True, null=True)
    chassis_or_truck_manufacturer_other = models.CharField(max_length=255, null=True, blank=True, verbose_name='Otra Marca')
    model = models.CharField(max_length=255, null=True, blank=True, verbose_name='Modelo')
    # Alternativas: Camiva, Rosenbauer, Magirus, E-One, Pierce, Crimson, Iturry u otro (agregar texto en otro)
    fk_carrosado_manufacturer = models.ForeignKey('VehicleCarrosadoManufacturer', verbose_name='Marca Carrosado', blank=True, null=True)
    carrosado_manufacturer_other = models.CharField(max_length=255, null=True, blank=True, verbose_name='Otra Marca')
    fk_condition = models.ForeignKey('Condition', verbose_name='Estado/Condición', null=True, blank=True, help_text='Si esta en reparación, dar el detalle en Observaciones')
    YEAR_CHOICE = [(year, year) for year in xrange(2011, 1949, -1)]
    vehicle_year = models.IntegerField(choices=YEAR_CHOICE, default=0, verbose_name='Año del vehículo')
    service_incorporation_date = models.DateField(blank = True, null = True, verbose_name='Fecha incorporación al servicio')
    # Estado de incorporación: Nuevo o usado
    fk_incorporation_status = models.ForeignKey('IncorporationStatus', verbose_name='Estado de incorporación', null=True, blank=True)
    previous_owner = models.CharField(max_length=255, null=True, blank=True, verbose_name='Propietario anterior')
    fk_color = models.ForeignKey('Color', verbose_name='Color', null=True, blank=True)
    # N° chassis, N° motor son string que contienen numeros y letras
    chassis_number = models.CharField(max_length=255, null=True, blank=True, verbose_name='N° Chassis')
    motor_number = models.CharField(max_length=255, null=True, blank=True, verbose_name='N° Motor')
    fk_transmission_type = models.ForeignKey('TransmissionType', verbose_name='Tipo de caja de cambio', null=True, blank=True)
    # motor_type/Tipo de motor se refiere a la pregunta de "Combustible" de la ficha original
    motor_type = models.ForeignKey('MotorType', verbose_name='Tipo de motor (Combustible)', null=True, blank=True)
    fk_procedence = models.ForeignKey('VehicleProcedence', verbose_name='Procedencia', null=True, blank=True)
    
    # Situacion legal
    
    registered = models.NullBooleanField(verbose_name='Inscrito')
    licence_plate = models.CharField(max_length=255, null=True, blank=True, verbose_name='Patente')

    #fk_vehicle_registration = models.ForeignKey('VehicleRegistrationStatus', verbose_name='Permiso de Circulación', null=True, blank=True)
    vehicle_registration = models.NullBooleanField(verbose_name='Permiso de Circulación')
    #fk_vehicle_checkup = models.ForeignKey('VehicleCheckupStatus', verbose_name='Revisión Técnica', null=True, blank=True)
    vehicle_checkup = models.NullBooleanField(verbose_name='Revisión Técnica')
    
    # Kilometraje y Horometraje
    
    kilometraje = models.IntegerField(null=True, blank=True, verbose_name='Kilometraje (Kms)')
    horometraje = models.IntegerField(null=True, blank=True, verbose_name='Horometraje (Hrs de trabajo de la bomba)')
       
    # Caracteristicas
    
    # Opciones: Camiva CB90, Camiva CH90, Camiva CB180, Camiva CH180, Camiva Otro modelo, Otra Marca (indicar marca y modelo)
    fk_fire_engine_camiva_model = models.ForeignKey('FireEngineCamivaModel', verbose_name='Marca Camiva', null=True, blank=True)
    fire_engine_other_manufacturer = models.CharField(max_length=255, null=True, blank=True, verbose_name='Otra Marca')
    fire_engine_other_model = models.CharField(max_length=255, null=True, blank=True, verbose_name='Otro Modelo')
    last_oil_change_date = models.DateField(blank = True, null = True, verbose_name='Fecha último cambio de aceite')
    oil_change_kilometraje = models.IntegerField(null=True, blank=True, verbose_name='Kilometraje del cambio de aceite')
    
    # Grandes reparaciones
    
    # Cambio Motor
    motor_change_new_manufacturer = models.CharField(max_length=255, null=True, blank=True, verbose_name='Marca')
    motor_change_new_model = models.CharField(max_length=255, null=True, blank=True, verbose_name='Modelo')
    motor_change_new_number = models.CharField(max_length=255, null=True, blank=True, verbose_name='Número')
    # Cambio Caja de cambio
    gearbox_change_new_manufacturer = models.CharField(max_length=255, null=True, blank=True, verbose_name='Marca')
    gearbox_change_new_model = models.CharField(max_length=255, null=True, blank=True, verbose_name='Modelo')
    # Reparación
    motor_repairs = models.NullBooleanField(verbose_name='Reparación Motor')
    gearbox_repairs = models.NullBooleanField(verbose_name='Reparación Caja de cambio')
    
    # Equipos de radio instalados en el carro
    
    truck_radio_equipment_quantity = models.IntegerField(null=True, blank=True, verbose_name='Cantidad')
    truck_radio_equipment_manufacturer = models.CharField(max_length=255, null=True, blank=True, verbose_name='Marca')
    truck_radio_equipment_model = models.CharField(max_length=255, null=True, blank=True, verbose_name='Modelo')
    truck_radio_equipment_power = models.IntegerField(null=True, blank=True, verbose_name='Potencia (W)')
    
    # Equipos de radio portátiles
    
    portable_radio_equipment_quantity = models.IntegerField(null=True, blank=True, verbose_name='Cantidad')
    portable_radio_equipment_manufacturer = models.CharField(max_length=255, null=True, blank=True, verbose_name='Marca')
    portable_radio_equipment_model = models.CharField(max_length=255, null=True, blank=True, verbose_name='Modelo')
    
    # Antenna
    
    antenna_quantity = models.IntegerField(null=True, blank=True, verbose_name='Cantidad')
    antenna_manufacturer = models.CharField(max_length=255, null=True, blank=True, verbose_name='Marca')
    antenna_model = models.CharField(max_length=255, null=True, blank=True, verbose_name='Modelo')
    antenna_decibels = models.IntegerField(null=True, blank=True, verbose_name='Decibeles')

    # Iluminación

    electricgenerator_fixed_in_car_quantity=models.IntegerField(null=True, blank=True, verbose_name='Nº de Generadores Electricos Fijos en Carros')
    fk_electricgenerator_fixed_in_car_potency=models.ForeignKey('PotencyRange', null=True, blank=True, verbose_name='Potencia de los Generadores Electricos Fijos en Carros', related_name='+')
    electricgenerator_portable_quantity=models.IntegerField(null=True, blank=True, verbose_name='Nº de Generadores Electricos Portátiles')
    fk_electricgenerator_portable_potency=models.ForeignKey('PotencyRange', null=True, blank=True, verbose_name='Potencia de los Generadores Electricos Portátiles', related_name='+')
    electricgenerator_fixed_in_barracks_quantity=models.IntegerField(null=True, blank=True, verbose_name='Nº de Generadores Electricos Fijos en cuarteles')
    fk_electricgenerator_fixed_in_barracks_potency=models.ForeignKey('PotencyRange', null=True, blank=True, verbose_name='Potencia de los Generadores Electricos Fijos en cuarteles', related_name='+')
    
    # Fotografías requeridas
    
    picture_front_view = ImageField(upload_to = 'cuerpo_mayor_material_pics', verbose_name=u'Vista Frontal', blank=True, null=True)
    picture_side_view = ImageField(upload_to = 'cuerpo_mayor_material_pics', verbose_name=u'Vista Lateral', blank=True, null=True)
    picture_back_view = ImageField(upload_to = 'cuerpo_mayor_material_pics', verbose_name=u'Vista Trasera', blank=True, null=True)
    
    # Observaciones
    
    observations = models.TextField(null=True, blank=True, verbose_name='')
