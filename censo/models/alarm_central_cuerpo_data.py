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
    telephoneexchange_electricalsupport= models.NullBooleanField(verbose_name='Respaldo Eléctrico de la Central Telefónica')
    telephoneexchange_satellitesupport= models.NullBooleanField(verbose_name='Respaldo Satelital de la Central Telefónica')
    telephoneexchange_satellitesupport_mark= models.CharField(max_length=255, null=True, blank=True, verbose_name='Marca del Respaldo Satelital de la Central Telefónica')
    telephonelines_enable_quantity = models.IntegerField(null=True, blank=True, verbose_name=u'Líneas de telefonos habilitadas')
    telephonelines_output_quantity = models.IntegerField(null=True, blank=True, verbose_name=u'Líneas de salidas de telefonos')
    telephonelines_input_quantity = models.IntegerField(null=True, blank=True, verbose_name=u'Líneas de entradas de telefonos')

    telephone_number132_available = models.NullBooleanField(verbose_name=u'¿Tiene el 132 habilitado?')
    call_log= models.NullBooleanField(verbose_name='Registro de llamadas')
    call_recording=models.NullBooleanField(verbose_name=u'Grabación de llamadas')
    cell_equipment_quantity = models.IntegerField(null=True, blank=True, verbose_name=u'Nº de equipos de celulares')

    #Equipos de Radio (Fijos)

    #Bases. Dinamico
    #Antenas Fijas
    fixed_antenna_quantity1 = models.IntegerField(default=0, verbose_name='Cantidad')
    fixed_antenna_manufacturer1 = models.CharField(max_length = 100, verbose_name='Marca', blank=True, null=True)
    fixed_antenna_model1 = models.CharField(max_length = 100, verbose_name='Modelo', blank=True, null=True)
    fixed_antenna_decibel1 = models.IntegerField(default=0, verbose_name='Decibeles')
    fixed_antenna_height1 = models.IntegerField(default=0, verbose_name='Altura (mts)')

    fixed_antenna_quantity2 = models.IntegerField(default=0, verbose_name='Cantidad')
    fixed_antenna_manufacturer2 = models.CharField(max_length = 100, verbose_name='Marca', blank=True, null=True)
    fixed_antenna_model2 = models.CharField(max_length = 100, verbose_name='Modelo', blank=True, null=True)
    fixed_antenna_decibel2 = models.IntegerField(default=0, verbose_name='Decibeles')
    fixed_antenna_height2 = models.IntegerField(default=0, verbose_name='Altura (mts)')

    #Generador de Tonos
    tone_generator_mark=models.CharField(max_length=255, null=True, blank=True, verbose_name='Marca del Generador de Tonos')
    tone_generator_capacity=models.IntegerField(null=True, blank=True, verbose_name='Capacidad de Compañias (max. para despacho) del Generador de Tonos')

    #Portátiles (Uso exclusivo de la Central)
    portable_quantity1 = models.IntegerField(default=0, verbose_name='Cantidad')
    fk_portable_manufacturer1 = models.ForeignKey('PortableBrand', verbose_name='Marca', blank=True, null=True, related_name='+')
    portable_model1 = models.CharField(max_length = 100, verbose_name='Modelo', blank=True, null=True)
    portable_power1 = models.IntegerField(default=0, verbose_name='Potencia (W)')

    portable_quantity2 = models.IntegerField(default=0, verbose_name='Cantidad')
    fk_portable_manufacturer2 = models.ForeignKey('PortableBrand', verbose_name='Marca', blank=True, null=True, related_name='+')
    portable_model2 = models.CharField(max_length = 100, verbose_name='Modelo', blank=True, null=True)
    portable_power2 = models.IntegerField(default=0, verbose_name='Potencia (W)')

    portable_quantity3 = models.IntegerField(default=0, verbose_name='Cantidad')
    fk_portable_manufacturer3 = models.ForeignKey('PortableBrand', verbose_name='Marca', blank=True, null=True, related_name='+')
    portable_model3 = models.CharField(max_length = 100, verbose_name='Modelo', blank=True, null=True)
    portable_power3 = models.IntegerField(default=0, verbose_name='Potencia (W)')


    #Frecuencias
    #primera frecuencia es obligatoria porque todos los cuerpos tienen al menos una
    frequency_one=models.DecimalField(max_digits=6, decimal_places=3, default=0, verbose_name='Frecuencia 1 (Mhz)')
    frequency_two=models.DecimalField(max_digits=6, decimal_places=3,null=True, blank=True, verbose_name='Frecuencia 2 (Mhz)')
    frequency_three=models.DecimalField(max_digits=6, decimal_places=3,null=True, blank=True, verbose_name='Frecuencia 3 (Mhz)')
    frequency_four=models.DecimalField(max_digits=6, decimal_places=3,null=True, blank=True, verbose_name='Frecuencia 4 (Mhz)')

    #Tipo?
    #obligatoria
    #cambio de normalizada a autorizada subtel
    normalized_frequency = models.IntegerField(choices=((1,"No"),(2, u"Sí"), (3,u"En Trámite")), default=1, verbose_name='Autorizada Subtel')

    decree=models.IntegerField(null=True, blank=True, verbose_name='Nº Decreto')
    decree_date=models.DateField(null=True, blank=True, verbose_name='Fecha (otorgada)')
    bandwidth=models.IntegerField(choices=((1,"12.5 Mhz"),(2, u"25 Mhz")), default=1, verbose_name='Ancho de Banda')
    fk_vhf=models.ForeignKey('VHF', verbose_name='Tipo', null=True, blank=True)
    national_emergency_frequency= models.NullBooleanField(verbose_name='Frecuencia Nacional de Emergencia (150.250 Mhz)')


    #Soporte tecnológico

    #Hardware
    pc_quantity=models.IntegerField(null=True, blank=True, verbose_name='Nº de Pc  ó  Notebook')

    #Software
    fk_os = models.ForeignKey('OperatingSystem', verbose_name='Sistema Operativo (Ingrese el más usado)', null=True, blank=True)
    digital_maps = models.NullBooleanField(verbose_name='Mapas digitales')
    adm_digital_maps = models.NullBooleanField(verbose_name='Administración de mapas digitales')
    adm_dispatch = models.NullBooleanField(verbose_name='Administración de despachos')
    fk_origin_software = models.ForeignKey('OriginSystem', verbose_name='Origen del Software', null=True, blank=True)
    origin_software_other = models.CharField(max_length=255, null=True, blank=True, verbose_name='Otro origen del software (Empresa)')

    #Procedimientos (Ex - Administración/Documentación)
    alarm_classification = models.NullBooleanField(verbose_name='Clasificación de Alarmas (Acto de Servicio)')
    sectorization = models.NullBooleanField(verbose_name='Sectorización (Mapas)')
    fk_coded_alarm = models.ForeignKey('CodedAlarmType', verbose_name='Alarmas codificadas', blank=True, null=True)
    operations_manual= models.NullBooleanField(verbose_name='Manual de Operaciones (Fisico)')
    key_coding=models.NullBooleanField(verbose_name='Codificación de Claves (Oficiales y Voluntarios)')
    fk_coded_keys = models.ForeignKey('CodedKeysType', verbose_name='Codificación para Material Mayor', blank=True, null=True)

    #Internet
    fk_internet_provider = models.ForeignKey('InternetProvider', verbose_name='Proveedor de Internet', blank=True, null=True)

    #Energía de Respaldo - (Solo Central)
    type_backup_power = models.CharField(max_length=255, null=True, blank=True, verbose_name='Tipo')
    potency_backup_power = models.CharField(max_length=255, null=True, blank=True, verbose_name='Potencia')
    autonomy_backup_power = models.CharField(max_length=255, null=True, blank=True, verbose_name='Autonomía')
    energizing_backup_power = models.CharField(max_length=255, null=True, blank=True, verbose_name='Que energiza')

    #Observaciones
    observations = models.TextField(null=True, blank=True, verbose_name='')
