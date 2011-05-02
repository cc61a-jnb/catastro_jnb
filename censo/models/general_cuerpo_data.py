# coding: utf-8

from django.db import models

class CuerpoGeneralData(models.Model):
    cuerpo = models.OneToOneField('censo.Cuerpo', blank=True)

    def __unicode__(self):
        return self.cuerpo.name

    class Meta:
        ordering = ['cuerpo']
        app_label = 'censo'
    
    # Hardware
    
    computers_quantity = models.IntegerField(null=True, blank=True, verbose_name='Computadores')
    notebooks_quantity = models.IntegerField(null=True, blank=True, verbose_name='Notebooks')
    projectors_quantity = models.IntegerField(null=True, blank=True, verbose_name='Proyectores')
    printers_quantity = models.IntegerField(null=True, blank=True, verbose_name='Impresoras')
    
    fk_internet_provider = models.ForeignKey('InternetProvider', verbose_name='Proveedor de Internet', blank=True, null=True)
    
    # Uso de tecnologías de internet
    
    website = models.URLField(null=True, blank=True, verbose_name='Sitio Web')
    social_facebook_account_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Cuenta Facebook')
    social_twitter_account_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Cuenta Twitter')
    social_other_account_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Otro')
    
    # Uso de sistema contable
    
    fk_accounting_system = models.ForeignKey('AccountingSystem', verbose_name='Sistema de contabilidad', blank=False, null=True)
    accounting_system_other_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Nombre Sistema contable')
    
    # Personal rentado
    
    personnel_guard = models.IntegerField(null=True, blank=True, verbose_name='Cuarteleros Cuidadores')
    personnel_driver = models.IntegerField(null=True, blank=True, verbose_name='Cuarteleros Conductores')
    personnel_secretary = models.IntegerField(null=True, blank=True, verbose_name='Secretarios')
    personnel_accounting = models.IntegerField(null=True, blank=True, verbose_name='Contadores')
    personnel_alarm_central_op = models.IntegerField(null=True, blank=True, verbose_name='Operadores Central de Alarmas')
    personnel_management = models.IntegerField(null=True, blank=True, verbose_name='Administrativos')
    personnel_mechanic = models.IntegerField(null=True, blank=True, verbose_name='Mecánicos de planta')
    personnel_cleaning = models.IntegerField(null=True, blank=True, verbose_name='Personal de Aseo')
    personnel_junior = models.IntegerField(null=True, blank=True, verbose_name='Servicios generales/Junior')
    
    # Observaciones
    
    observations = models.TextField(null=True, blank=True, verbose_name='')
