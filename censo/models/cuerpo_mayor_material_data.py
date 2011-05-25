# coding: utf-8

from django.db import models
from sorl.thumbnail import ImageField

class CuerpoMayorMaterialData(models.Model):
    cuerpo = models.ForeignKey('censo.Cuerpo')
    company = models.ForeignKey('censo.Company', null=True, blank=True)

    def __unicode__(self):
        return unicode(self.cuerpo)

    class Meta:
        get_latest_by = 'id'
        ordering = ['cuerpo', 'id']
        app_label = 'censo'
        
        
    # Informacion del vehiculo
     
    fk_vehicle_type = models.ForeignKey('VehicleType', verbose_name='Tipo de Vehículo', blank=True, null=True)
    denomination = models.CharField(max_length=255, null=True, blank=True, verbose_name='Denominación')
    chassis_or_truck_manufacturer = models.CharField(max_length=255, null=True, blank=True, verbose_name='Marca Chassis/Camión')
    model = models.CharField(max_length=255, null=True, blank=True, verbose_name='Modelo')
    carrosado_manufacturer = models.CharField(max_length=255, null=True, blank=True, verbose_name='Marca Carrosado')
    fk_condition = models.ForeignKey('Condition', verbose_name='Estado/Condición', null=True, blank=True)
    vehicle_year = models.IntegerField(null=True, blank=True, verbose_name='Año del vehículo')
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
    
    registered = models.BooleanField(verbose_name='Inscrito')
    licence_plate = models.CharField(max_length=255, null=True, blank=True, verbose_name='Patente')
    # Permiso de circulacion -> Opciones: Al dia, Vencido, No tiene
    fk_vehicle_registration = models.ForeignKey('VehicleRegistrationStatus', verbose_name='Permiso de Circulación', null=True, blank=True)
    # Revision tecnica -> Opciones: Al dia, Vencida, No tiene
    fk_vehicle_checkup = models.ForeignKey('VehicleCheckupStatus', verbose_name='Revisión Técnica', null=True, blank=True)
    
    # Kilometraje y Horometraje
    
    kilometraje = models.IntegerField(null=True, blank=True, verbose_name='Kilometraje (Kms)')
    horometraje = models.IntegerField(null=True, blank=True, verbose_name='Horometraje (Hrs de trabajo de la bomba)')
       
    # Caracteristicas
    
    fk_fire_engine_camiva_model = models.ForeignKey('FireEngineCamivaModel', verbose_name='Camiva', null=True, blank=True)
    fire_engine_other_manufacturer = models.CharField(max_length=255, null=True, blank=True, verbose_name='Marca')
    fire_engine_other_model = models.CharField(max_length=255, null=True, blank=True, verbose_name='Modelo')
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
    motor_repairs = models.BooleanField(verbose_name='Reparación Motor')
    gearbox_repairs = models.BooleanField(verbose_name='Reparación Caja de cambio')
    
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
    
    # Fotografías requeridas
    
    picture_front_view = ImageField(upload_to = 'cuerpo_mayor_material_pics', verbose_name=u'Vista Frontal', blank=True, null=True)
    picture_side_view = ImageField(upload_to = 'cuerpo_mayor_material_pics', verbose_name=u'Vista Lateral', blank=True, null=True)
    picture_back_view = ImageField(upload_to = 'cuerpo_mayor_material_pics', verbose_name=u'Vista Trasera', blank=True, null=True)
    
    # Observaciones
    
    observations = models.TextField(null=True, blank=True, verbose_name='')
