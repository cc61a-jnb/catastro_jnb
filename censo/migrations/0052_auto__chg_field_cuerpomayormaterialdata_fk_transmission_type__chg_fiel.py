# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Changing field 'CuerpoMayorMaterialData.fk_transmission_type'
        db.alter_column('censo_cuerpomayormaterialdata', 'fk_transmission_type_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['censo.TransmissionType'], null=True, blank=True))

        # Changing field 'CuerpoMayorMaterialData.fk_vehicle_registration'
        db.alter_column('censo_cuerpomayormaterialdata', 'fk_vehicle_registration_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['censo.VehicleRegistrationStatus'], null=True, blank=True))

        # Changing field 'CuerpoMayorMaterialData.fk_vehicle_checkup'
        db.alter_column('censo_cuerpomayormaterialdata', 'fk_vehicle_checkup_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['censo.VehicleCheckupStatus'], null=True, blank=True))

        # Changing field 'CuerpoMayorMaterialData.fk_incorporation_status'
        db.alter_column('censo_cuerpomayormaterialdata', 'fk_incorporation_status_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['censo.IncorporationStatus'], null=True, blank=True))

        # Changing field 'CuerpoMayorMaterialData.fk_procedence'
        db.alter_column('censo_cuerpomayormaterialdata', 'fk_procedence_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['censo.VehicleProcedence'], null=True, blank=True))

        # Changing field 'CuerpoMayorMaterialData.gearbox_repairs'
        db.alter_column('censo_cuerpomayormaterialdata', 'gearbox_repairs', self.gf('django.db.models.fields.BooleanField')(blank=True))

        # Changing field 'CuerpoMayorMaterialData.fk_fire_engine_camiva_model'
        db.alter_column('censo_cuerpomayormaterialdata', 'fk_fire_engine_camiva_model_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['censo.FireEngineCamivaModel'], null=True, blank=True))

        # Changing field 'CuerpoMayorMaterialData.fk_color'
        db.alter_column('censo_cuerpomayormaterialdata', 'fk_color_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['censo.Color'], null=True, blank=True))

        # Changing field 'CuerpoMayorMaterialData.registered'
        db.alter_column('censo_cuerpomayormaterialdata', 'registered', self.gf('django.db.models.fields.BooleanField')(blank=True))

        # Changing field 'CuerpoMayorMaterialData.motor_repairs'
        db.alter_column('censo_cuerpomayormaterialdata', 'motor_repairs', self.gf('django.db.models.fields.BooleanField')(blank=True))

        # Changing field 'CuerpoMayorMaterialData.motor_type'
        db.alter_column('censo_cuerpomayormaterialdata', 'motor_type_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['censo.MotorType'], null=True, blank=True))

        # Changing field 'CuerpoMayorMaterialData.fk_condition'
        db.alter_column('censo_cuerpomayormaterialdata', 'fk_condition_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['censo.Condition'], null=True, blank=True))
    
    
    def backwards(self, orm):
        
        # Changing field 'CuerpoMayorMaterialData.fk_transmission_type'
        db.alter_column('censo_cuerpomayormaterialdata', 'fk_transmission_type_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['censo.TransmissionType'], null=True))

        # Changing field 'CuerpoMayorMaterialData.fk_vehicle_registration'
        db.alter_column('censo_cuerpomayormaterialdata', 'fk_vehicle_registration_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['censo.VehicleRegistrationStatus'], null=True))

        # Changing field 'CuerpoMayorMaterialData.fk_vehicle_checkup'
        db.alter_column('censo_cuerpomayormaterialdata', 'fk_vehicle_checkup_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['censo.VehicleCheckupStatus'], null=True))

        # Changing field 'CuerpoMayorMaterialData.fk_incorporation_status'
        db.alter_column('censo_cuerpomayormaterialdata', 'fk_incorporation_status_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['censo.IncorporationStatus'], null=True))

        # Changing field 'CuerpoMayorMaterialData.fk_procedence'
        db.alter_column('censo_cuerpomayormaterialdata', 'fk_procedence_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['censo.VehicleProcedence'], null=True))

        # Changing field 'CuerpoMayorMaterialData.gearbox_repairs'
        db.alter_column('censo_cuerpomayormaterialdata', 'gearbox_repairs', self.gf('django.db.models.fields.BooleanField')())

        # Changing field 'CuerpoMayorMaterialData.fk_fire_engine_camiva_model'
        db.alter_column('censo_cuerpomayormaterialdata', 'fk_fire_engine_camiva_model_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['censo.FireEngineCamivaModel'], null=True))

        # Changing field 'CuerpoMayorMaterialData.fk_color'
        db.alter_column('censo_cuerpomayormaterialdata', 'fk_color_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['censo.Color'], null=True))

        # Changing field 'CuerpoMayorMaterialData.registered'
        db.alter_column('censo_cuerpomayormaterialdata', 'registered', self.gf('django.db.models.fields.BooleanField')())

        # Changing field 'CuerpoMayorMaterialData.motor_repairs'
        db.alter_column('censo_cuerpomayormaterialdata', 'motor_repairs', self.gf('django.db.models.fields.BooleanField')())

        # Changing field 'CuerpoMayorMaterialData.motor_type'
        db.alter_column('censo_cuerpomayormaterialdata', 'motor_type_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['censo.MotorType'], null=True))

        # Changing field 'CuerpoMayorMaterialData.fk_condition'
        db.alter_column('censo_cuerpomayormaterialdata', 'fk_condition_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['censo.Condition'], null=True))
    
    
    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'censo.accountingsystem': {
            'Meta': {'object_name': 'AccountingSystem'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'censo.bandwidth': {
            'Meta': {'object_name': 'BandWidth'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'censo.buildingmaterialtype': {
            'Meta': {'object_name': 'BuildingMaterialType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'censo.codedalarmtype': {
            'Meta': {'object_name': 'CodedAlarmType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'censo.codedkeystype': {
            'Meta': {'object_name': 'CodedKeysType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'censo.color': {
            'Meta': {'object_name': 'Color'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'censo.commune': {
            'Meta': {'object_name': 'Commune'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'old_id': ('django.db.models.fields.IntegerField', [], {}),
            'province': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.Province']"})
        },
        'censo.company': {
            'Meta': {'object_name': 'Company'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'commune': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'null': 'True', 'to': "orm['censo.Commune']"}),
            'cuerpo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cuerpo_company'", 'null': 'True', 'to': "orm['censo.Cuerpo']"}),
            'foundation_date': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'old_id': ('django.db.models.fields.IntegerField', [], {}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'censo.companyotherofficial': {
            'Meta': {'object_name': 'CompanyOtherOfficial'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.Company']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'role_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'censo.condition': {
            'Meta': {'object_name': 'Condition'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'censo.cuerpo': {
            'Meta': {'object_name': 'Cuerpo'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'commune': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['censo.Commune']"}),
            'decree_date': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'foundation_date': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'npers_juri': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'old_id': ('django.db.models.fields.IntegerField', [], {}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'censo.cuerpoalarmcentralbaseradioeq': {
            'Meta': {'object_name': 'CuerpoAlarmCentralBaseRadioEq'},
            'cuerpo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.Cuerpo']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manufacturer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.PortableBrand']", 'null': 'True', 'blank': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'power': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'censo.cuerpoalarmcentraldata': {
            'Meta': {'object_name': 'CuerpoAlarmCentralData'},
            'adm_digital_maps': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'adm_dispatch': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'adress_alarm_central': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'afternoon_roleshift_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'alarm_classification': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'autonomy_backup_power': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bandwidth': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'call_log': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'call_recording': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'cell_equipment_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cuerpo': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['censo.Cuerpo']", 'unique': 'True', 'blank': 'True'}),
            'decree': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'decree_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'digital_maps': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'email_alarm_central': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'energizing_backup_power': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'fax_alarm_central': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'fixed_antenna_decibel1': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'fixed_antenna_decibel2': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'fixed_antenna_height1': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'fixed_antenna_height2': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'fixed_antenna_manufacturer1': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'fixed_antenna_manufacturer2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'fixed_antenna_model1': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'fixed_antenna_model2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'fixed_antenna_quantity1': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'fixed_antenna_quantity2': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'fk_coded_alarm': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.CodedAlarmType']", 'null': 'True', 'blank': 'True'}),
            'fk_coded_keys': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.CodedKeysType']", 'null': 'True', 'blank': 'True'}),
            'fk_internet_provider': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.InternetProvider']", 'null': 'True', 'blank': 'True'}),
            'fk_origin_software': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.OriginSystem']", 'null': 'True', 'blank': 'True'}),
            'fk_os': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.OperatingSystem']", 'null': 'True', 'blank': 'True'}),
            'fk_portable_manufacturer1': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['censo.PortableBrand']"}),
            'fk_portable_manufacturer2': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['censo.PortableBrand']"}),
            'fk_portable_manufacturer3': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['censo.PortableBrand']"}),
            'fk_vhf': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.VHF']", 'null': 'True', 'blank': 'True'}),
            'frequency_four': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '3', 'blank': 'True'}),
            'frequency_one': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '6', 'decimal_places': '3'}),
            'frequency_three': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '3', 'blank': 'True'}),
            'frequency_two': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '3', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key_coding': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'national_emergency_frequency': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'night_roleshift_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'normalized_frequency': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'observations': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'operations_manual': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'operators_availableatalltimes_quantity': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'origin_software_other': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'pc_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'portable_model1': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'portable_model2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'portable_model3': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'portable_power1': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'portable_power2': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'portable_power3': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'portable_quantity1': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'portable_quantity2': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'portable_quantity3': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'potency_backup_power': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'sectorization': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'telephone_alarm_central': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'telephone_number132_available': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'telephoneexchange_electricalsupport': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'telephoneexchange_satellitesupport': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'telephoneexchange_satellitesupport_mark': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'telephonelines_enable_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'telephonelines_input_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'telephonelines_output_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tomorrow_roleshift_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tone_generator_capacity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tone_generator_mark': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'type_backup_power': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'censo.cuerpoanbdata': {
            'Meta': {'object_name': 'CuerpoANBData'},
            'anb_health_instructors': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'anb_procedure_instructors': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'anb_specialty_instructors': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cuerpo': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['censo.Cuerpo']", 'unique': 'True', 'blank': 'True'}),
            'cuerpo_brigada_juvenil_antiquity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cuerpo_brigada_juvenil_members_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cuerpo_brigada_juvenil_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'cuerpo_brigada_juvenil_responsible_email': ('django.db.models.fields.EmailField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'cuerpo_brigada_juvenil_responsible_nombre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'cuerpo_brigada_juvenil_responsible_role': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'cuerpo_courses_infrastructure_amplifiers': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cuerpo_courses_infrastructure_boards': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cuerpo_courses_infrastructure_datashow': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cuerpo_courses_infrastructure_diapositives': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cuerpo_courses_infrastructure_rcp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cuerpo_courses_infrastructure_rooms': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cuerpo_courses_infrastructure_telon': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cuerpo_courses_infrastructure_transparencies': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cuerpo_courses_infrastructure_tvs': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cuerpo_courses_infrastructure_video': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cuerpo_health_instructors': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cuerpo_procedure_instructors': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cuerpo_specialty_instructors': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'observations': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'censo.cuerpogeneraldata': {
            'Meta': {'object_name': 'CuerpoGeneralData'},
            'accounting_system_other_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'computers_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cuerpo': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['censo.Cuerpo']", 'unique': 'True', 'blank': 'True'}),
            'fk_accounting_system': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.AccountingSystem']", 'null': 'True'}),
            'fk_internet_provider': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.InternetProvider']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notebooks_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'observations': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'personnel_accounting': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'personnel_alarm_central_op': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'personnel_cleaning': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'personnel_driver': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'personnel_guard': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'personnel_junior': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'personnel_management': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'personnel_mechanic': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'personnel_secretary': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'printers_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'projectors_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'social_facebook_account_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'social_other_account_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'social_twitter_account_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'censo.cuerpoinfrastructuredata': {
            'Meta': {'object_name': 'CuerpoInfrastructureData'},
            'barrack_house': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'bathrooms': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'building_extension_construction_legal': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'building_extension_construction_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'building_initial_construction_legal': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'building_initial_construction_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'building_material_type': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['censo.BuildingMaterialType']", 'null': 'True', 'blank': 'True'}),
            'built_area_back_m2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'built_area_front_m2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'built_area_surface_m2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'built_area_total_m2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cafeteria': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'cuerpo': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['censo.Cuerpo']", 'unique': 'True', 'blank': 'True'}),
            'fk_property_title_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.PropertyTitleType']", 'null': 'True', 'blank': 'True'}),
            'general_secretary_office': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'general_treasurer_office': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inscription_fojas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'inscription_number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'inscription_owner_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'inscription_real_estate_registrar': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'inscription_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'kitchen': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'living_room': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'main_street_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'major_office': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'narrow_street_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'observations': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'others': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'picture_back_view': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'picture_front_view': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'picture_general_view': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'picture_internal_distribution_view': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'picture_machine_room_view': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'picture_office_view': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'property_commodatum_end_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rol_sii': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'secondary_street_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'storage': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'supervisor_office': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'terrain_machine_room_m2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'terrain_session_room_m2': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'})
        },
        'censo.cuerpoinfrastructureotheroffices': {
            'Meta': {'object_name': 'CuerpoInfrastructureOtherOffices'},
            'cuerpo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.Cuerpo']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'role_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'censo.cuerpomayormaterialdata': {
            'Meta': {'object_name': 'CuerpoMayorMaterialData'},
            'antenna_decibels': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'antenna_manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'antenna_model': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'antenna_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'carrosado_manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'chassis_number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'chassis_or_truck_manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.Company']", 'null': 'True', 'blank': 'True'}),
            'cuerpo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.Cuerpo']"}),
            'denomination': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'fire_engine_other_manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'fire_engine_other_model': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'fk_color': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.Color']", 'null': 'True', 'blank': 'True'}),
            'fk_condition': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.Condition']", 'null': 'True', 'blank': 'True'}),
            'fk_fire_engine_camiva_model': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.FireEngineCamivaModel']", 'null': 'True', 'blank': 'True'}),
            'fk_incorporation_status': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.IncorporationStatus']", 'null': 'True', 'blank': 'True'}),
            'fk_procedence': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.VehicleProcedence']", 'null': 'True', 'blank': 'True'}),
            'fk_transmission_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.TransmissionType']", 'null': 'True', 'blank': 'True'}),
            'fk_vehicle_checkup': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.VehicleCheckupStatus']", 'null': 'True', 'blank': 'True'}),
            'fk_vehicle_registration': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.VehicleRegistrationStatus']", 'null': 'True', 'blank': 'True'}),
            'fk_vehicle_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.VehicleType']", 'null': 'True', 'blank': 'True'}),
            'gearbox_change_new_manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'gearbox_change_new_model': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'gearbox_repairs': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'horometraje': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kilometraje': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'last_oil_change_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'licence_plate': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'motor_change_new_manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'motor_change_new_model': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'motor_change_new_number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'motor_number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'motor_repairs': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'motor_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.MotorType']", 'null': 'True', 'blank': 'True'}),
            'observations': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'oil_change_kilometraje': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'picture_back_view': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'picture_front_view': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'picture_side_view': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'portable_radio_equipment_manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'portable_radio_equipment_model': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'portable_radio_equipment_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'previous_owner': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'registered': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'service_incorporation_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'truck_radio_equipment_manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'truck_radio_equipment_model': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'truck_radio_equipment_power': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'truck_radio_equipment_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'vehicle_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'censo.cuerpootherofficial': {
            'Meta': {'object_name': 'CuerpoOtherOfficial'},
            'cuerpo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.Cuerpo']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'role_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'censo.cuerposerviceactsdata': {
            'Meta': {'object_name': 'CuerpoServiceActsData'},
            'cuerpo': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['censo.Cuerpo']", 'unique': 'True', 'blank': 'True'}),
            'debris_removal_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'electrical_emergency_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'incidents_combustible_gases_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'incidents_explosive_materials_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'observations': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'other_emergencies_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'outdoors_fire_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rescue_victims_not_vehicles_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rescue_victims_vehicles_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'revision_inspection_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'structural_fire_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'support_other_cuerpos_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'vehicles_fire_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'censo.fireenginecamivamodel': {
            'Meta': {'object_name': 'FireEngineCamivaModel'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'censo.incorporationstatus': {
            'Meta': {'object_name': 'IncorporationStatus'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'censo.infrastructurecompanydata': {
            'Meta': {'object_name': 'InfrastructureCompanyData'},
            'barrack_house_bathroom': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'barrack_house_bedroom': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'barrack_house_kitchen': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'building_extension_construction_legal': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'building_extension_construction_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'building_initial_construction_legal': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'building_initial_construction_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'building_material_type': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['censo.BuildingMaterialType']", 'null': 'True', 'blank': 'True'}),
            'built_area_back_m2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'built_area_front_m2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'built_area_surface_m2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'built_area_total_m2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cafeteria': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'captain_office': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'common_bathrooms': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'common_offices': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'company': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['censo.Company']", 'unique': 'True', 'blank': 'True'}),
            'director_office': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'fk_property_title_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.PropertyTitleType']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inscription_fojas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'inscription_number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'inscription_owner_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'inscription_real_estate_registrar': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'inscription_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'kitchen': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'lieutenant_office': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'living_room': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'main_street_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'men_bathroom': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'narrow_street_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'night_guard_office_kitchen': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'night_guard_office_men_bathroom': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'night_guard_office_men_bathroom_showers': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'night_guard_office_men_bathroom_urinary': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'night_guard_office_men_bathroom_wc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'night_guard_office_men_beds': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'night_guard_office_women_bathroom': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'night_guard_office_women_bathroom_showers': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'night_guard_office_women_bathroom_wc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'night_guard_office_women_beds': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'observations': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'officers_office': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'others': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'picture_back_view': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'picture_front_view': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'picture_general_view': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'picture_internal_distribution_view': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'picture_machine_room_view': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'picture_office_view': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'property_rental_commodatum_end_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rol_sii': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'secondary_street_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'secretary_office': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'storage': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'terrain_machine_room_m2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'terrain_session_room_m2': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'treasurer_office': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'women_bathroom': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'})
        },
        'censo.internetprovider': {
            'Meta': {'object_name': 'InternetProvider'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'censo.minormaterialcompanydata': {
            'Meta': {'object_name': 'MinorMaterialCompanyData'},
            'aircompressor_bycar_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'aircompressor_fixed_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'airmattresses_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'antenna_equipment_manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'antenna_equipment_model': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'antenna_equipment_power': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'antenna_equipment_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'base_radio_equipment_manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'base_radio_equipment_model': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'base_radio_equipment_power': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'base_radio_equipment_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cascade_bycar_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cascade_cylinder_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cascade_fixed_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'chainsaw_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'company': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['censo.Company']", 'unique': 'True', 'blank': 'True'}),
            'containers_proteinconcentrate_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'containers_syntheticconcentrate_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'defibrillator_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'electricgenerator_fixed_in_barracks_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'electricgenerator_fixed_in_car_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'electricgenerator_portable_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fensy_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fireman_shoes_company_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fireman_shoes_volunteer_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'firesfans_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fk_electricgenerator_fixed_in_barracks_potency': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['censo.PotencyRange']"}),
            'fk_electricgenerator_fixed_in_car_potency': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['censo.PotencyRange']"}),
            'fk_electricgenerator_portable_potency': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['censo.PotencyRange']"}),
            'foam_generating_equipment_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'generators_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gloves_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hazmat_seal_kits_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'helmets_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hosepipe_38mm_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hosepipe_50mm_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hosepipe_70mm_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hosepipe_forest_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hydraulic_equipment_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instruments_for_detection_of_combustible_gases_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'instruments_of_toxic_gas_analysis_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'jackets_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'levelA_chemical_protection_suits_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'levelB_chemical_protection_suits_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mSA_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'motorpump_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'observations': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'oxygen_equipment_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pants_or_overalls_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'portable_radio_equipment_manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'portable_radio_equipment_model': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'portable_radio_equipment_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'protective_clothing_coated_aluminized_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'python_50adjustable_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'python_50tube_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'python_70adjustable_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'python_70tube_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'racal_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'scott_after_2004_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'scott_before_2004_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'short_capes_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tripok_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'twins_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'censo.motortype': {
            'Meta': {'object_name': 'MotorType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'censo.normalizedfrequency': {
            'Meta': {'object_name': 'NormalizedFrequency'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'censo.occupation': {
            'Meta': {'object_name': 'Occupation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'})
        },
        'censo.operatingsystem': {
            'Meta': {'object_name': 'OperatingSystem'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'censo.originsystem': {
            'Meta': {'object_name': 'OriginSystem'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'censo.portablebrand': {
            'Meta': {'object_name': 'PortableBrand'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'censo.portadacompanydata': {
            'Meta': {'object_name': 'PortadaCompanyData'},
            'assistant_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'captain_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'company': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['censo.Company']", 'unique': 'True'}),
            'director_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lieutenant_1_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'lieutenant_2_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'lieutenant_3_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'lieutenant_4_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'observations': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'secretary_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'tesorero_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'censo.portadacuerpodata': {
            'Meta': {'object_name': 'PortadaCuerpoData'},
            'commander_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'cuerpo': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['censo.Cuerpo']", 'unique': 'True', 'blank': 'True'}),
            'forth_commander_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intendent_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'observations': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'second_commander_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'secretary_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'superintendent_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'third_commander_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'treasury_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'vice_superintendent_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'censo.potencyrange': {
            'Meta': {'object_name': 'PotencyRange'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'censo.propertytitletype': {
            'Meta': {'object_name': 'PropertyTitleType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'censo.province': {
            'Meta': {'object_name': 'Province'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'old_id': ('django.db.models.fields.IntegerField', [], {}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.Region']"})
        },
        'censo.region': {
            'Meta': {'object_name': 'Region'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'old_id': ('django.db.models.fields.IntegerField', [], {})
        },
        'censo.speciality': {
            'Meta': {'object_name': 'Speciality'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'censo.transmissiontype': {
            'Meta': {'object_name': 'TransmissionType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'censo.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.Company']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'old_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.Region']", 'null': 'True', 'blank': 'True'}),
            'role_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'role_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'censo.vehiclecheckupstatus': {
            'Meta': {'object_name': 'VehicleCheckupStatus'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'censo.vehicleprocedence': {
            'Meta': {'object_name': 'VehicleProcedence'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'censo.vehicleregistrationstatus': {
            'Meta': {'object_name': 'VehicleRegistrationStatus'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'censo.vehicletype': {
            'Meta': {'object_name': 'VehicleType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'censo.vhf': {
            'Meta': {'object_name': 'VHF'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'censo.volunteerdata': {
            'Meta': {'object_name': 'VolunteerData'},
            'company': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['censo.Company']", 'unique': 'True', 'blank': 'True'}),
            'computers_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fk_internet_provider': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.InternetProvider']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notebooks_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'observations': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'printers_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'projectors_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'social_facebook_account_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'social_other_account_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'social_twitter_account_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'specialities': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['censo.Speciality']", 'null': 'True', 'blank': 'True'}),
            'specialities_other': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'volunteer_active_men_quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'volunteer_active_women_quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'volunteer_age_60_or_more_men_quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'volunteer_age_60_or_more_women_quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'volunteer_age_between_18_25_men_quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'volunteer_age_between_18_25_women_quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'volunteer_age_between_26_30_men_quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'volunteer_age_between_26_30_women_quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'volunteer_age_between_31_35_men_quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'volunteer_age_between_31_35_women_quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'volunteer_age_between_36_40_men_quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'volunteer_age_between_36_40_women_quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'volunteer_age_between_41_45_men_quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'volunteer_age_between_41_45_women_quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'volunteer_age_between_46_50_men_quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'volunteer_age_between_46_50_women_quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'volunteer_age_between_51_55_men_quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'volunteer_age_between_51_55_women_quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'volunteer_age_between_56_60_men_quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'volunteer_age_between_56_60_women_quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'volunteer_antiquity_required_to_honorary': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'volunteer_brigada_juvenil_antiquity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'volunteer_brigada_juvenil_members_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'volunteer_brigada_juvenil_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'volunteer_brigada_juvenil_responsible_email': ('django.db.models.fields.EmailField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'volunteer_brigada_juvenil_responsible_instructor': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'volunteer_class_f_bomberos_driver_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'volunteer_class_f_cuarteleros_driver_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'volunteer_education_basica_complete_quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'volunteer_education_media_complete_quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'volunteer_education_tecnica_complete_quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'volunteer_education_universitaria_complete_quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'volunteer_gt_than_3_years_academia_course_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'volunteer_gt_than_3_years_cuerpo_course_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'volunteer_hoja_de_vida_cargo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'volunteer_hoja_de_vida_email': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'volunteer_hoja_de_vida_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'volunteer_hoja_de_vida_phone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'volunteer_honorary_men_quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'volunteer_honorary_women_quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'volunteer_lt_than_3_years_academia_course_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'volunteer_lt_than_3_years_cuerpo_course_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'volunteer_total_men_quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'volunteer_total_women_quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'volunteer_with_work_quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }
    
    complete_apps = ['censo']
