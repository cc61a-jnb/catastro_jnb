# coding: utf-8

from django.db import models

class CuerpoAlarmCentralData(models.Model):

    cuerpo = models.OneToOneField('censo.Cuerpo', blank=True)

    def __unicode__(self):
        return self.cuerpo.name

    class Meta:
        ordering = ['cuerpo']
        app_label = 'censo'

    #Datos de contacto
    adress_alarm_central = models.CharField(max_length=255, null=True, blank=True, verbose_name='Dirección')
    telephone_alarm_central= models.CharField(max_length=255, null=True, blank=True, verbose_name='Teléfono')
    fax_alarm_central=models.CharField(max_length=255, null=True, blank=True, verbose_name='Fax')
    email_alarm_central=models.CharField(max_length=255, null=True, blank=True, verbose_name='Email')
 
    #Personal (operadoras)
    tomorrow_roleshift_quantity = models.IntegerField(null=True, blank=True, verbose_name='Nº Mañana')
    afternoon_roleshift_quantity = models.IntegerField(null=True, blank=True, verbose_name='Nº Tarde')
    night_roleshift_quantity = models.IntegerField(null=True, blank=True, verbose_name='Nº Noche')
    operators_availableatalltimes_quantity = models.NullBooleanField(verbose_name='Operadoras 24/7/365')
    
    #Telefonía (mesa)
    telephoneexchange_electricalsupport= models.NullBooleanField(verbose_name='Respaldo Electrico de la Central Telefónica')
    telephoneexchange_satellitesupport= models.NullBooleanField(verbose_name='Respaldo Satelital de la Central Telefónica')
    telephoneexchange_satellitesupport_mark= models.CharField(max_length=255, null=True, blank=True, verbose_name='Marca del Respaldo Satelital de la Central Telefónica')
    telephonelines_enable_quantity = models.IntegerField(null=True, blank=True, verbose_name='Líneas de telefonos habilitadas')
    telephonelines_output_quantity = models.IntegerField(null=True, blank=True, verbose_name='Líneas de salidas de telefonos')
    telephonelines_input_quantity = models.IntegerField(null=True, blank=True, verbose_name='Líneas de entradas de telefonos')
    call_log= models.NullBooleanField(verbose_name='Registro de llamadas')
    call_recording=models.NullBooleanField(verbose_name='Grabación de llamadas')
    cell_equipment_quantity = models.IntegerField(null=True, blank=True, verbose_name='Nº de equipos de celulares')

    #Equipos de Radio (Fijos)
    
    #Bases. Dinamico
    #Antenas Fijas. Dinamico
    #Generador de Tonos
    tone_generator_mark=models.CharField(max_length=255, null=True, blank=True, verbose_name='Marca del Generador de Tonos')
    tone_generator_capacity=models.IntegerField(null=True, blank=True, verbose_name='Capacidad de Compañias (max. para despacho) del Generador de Tonos')

    #Portátiles (Uso exclusivo de la Central). Dinamico
    
    #Frecuencias
    frequency_one=models.IntegerField(null=True, blank=True, verbose_name='Frecuencia 1 (mghz)')
    frequency_two=models.IntegerField(null=True, blank=True, verbose_name='Frecuencia 2 (mghz)')
    frequency_three=models.IntegerField(null=True, blank=True, verbose_name='Frecuencia 3 (mghz)')
    frequency_four=models.IntegerField(null=True, blank=True, verbose_name='Frecuencia 4 (mghz)')
    
    #Tipo?
    fk_normalized_frequency = models.ForeignKey('NormalizedFrequency', verbose_name='normalizada', null=True, blank=False)
    decree=models.IntegerField(null=True, blank=True, verbose_name='Nº Decreto')
    date=models.IntegerField(null=True, blank=True, verbose_name='Fecha (otorgada)')
    fk_bandwidth=models.ForeignKey('BandWidth', verbose_name='Ancho de Banda', null=True, blank=False)
    fk_vhf=models.ForeignKey('VHF', verbose_name='Rango de Frecuencia', null=True, blank=False)
    national_emergency_frequency= models.NullBooleanField(verbose_name='Frecuencia Nacional de Emergencia')


    #Soporte tecnológico
    
    #Hardware 
    pc_quantity=models.IntegerField(null=True, blank=True, verbose_name='Nº de Pc  ó  Notebook')

    #Software
    fk_os = models.ForeignKey('OperatingSystem', verbose_name='Sistema Operativo', null=True, blank=False)
    digital_maps = models.NullBooleanField(verbose_name='Mapas digitales')
    adm_digital_maps = models.NullBooleanField(verbose_name='Administración de mapas digitales')
    adm_dispatch = models.NullBooleanField(verbose_name='Administración de despachos')
    fk_origin_software = models.ForeignKey('OriginSystem', verbose_name='Origen del Software', null=True, blank=False)
    origin_software_other = models.CharField(max_length=255, null=True, blank=True, verbose_name='Otro origen del software (Empresa)')
    
    #Administración - Documentación
    alarm_classification = models.NullBooleanField(verbose_name='Clasificación de Alarmas (Acto de Servicio)')
    sectorization = models.NullBooleanField(verbose_name='Sectorización (Mapas)')
    fk_coded_alarm = models.ForeignKey('CodedAlarmType', verbose_name='Alarmas codificadas', blank=True, null=True)
    operations_manual= models.NullBooleanField(verbose_name='Manual de Operaciones (Fisico)')
    key_coding=models.NullBooleanField(verbose_name='Codificación de Claves (Oficiales y Voluntario)')
    fk_coded_keys = models.ForeignKey('CodedKeysType', verbose_name='Codificación de Claves (Oficiales y Voluntarios)', blank=True, null=True)
    
    #Internet
    fk_internet_provider = models.ForeignKey('InternetProvider', verbose_name='Proveedor de Internet', blank=True, null=True)
    
    #Energía de Respaldo - (Solo Central)
    type_backup_power = models.CharField(max_length=255, null=True, blank=True, verbose_name='Tipo')
    potency_backup_power = models.CharField(max_length=255, null=True, blank=True, verbose_name='Potencia')
    autonomy_backup_power = models.CharField(max_length=255, null=True, blank=True, verbose_name='Autonomía')
    energizing_backup_power = models.CharField(max_length=255, null=True, blank=True, verbose_name='Que energiza')
    
    #Observaciones
    observations = models.TextField(null=True, blank=True, verbose_name='')
