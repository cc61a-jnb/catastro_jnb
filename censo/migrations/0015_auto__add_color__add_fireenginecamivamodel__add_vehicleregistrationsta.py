# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Color'
        db.create_table('censo_color', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('censo', ['Color'])

        # Adding model 'FireEngineCamivaModel'
        db.create_table('censo_fireenginecamivamodel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('censo', ['FireEngineCamivaModel'])

        # Adding model 'VehicleRegistrationStatus'
        db.create_table('censo_vehicleregistrationstatus', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('censo', ['VehicleRegistrationStatus'])

        # Adding model 'TransmissionType'
        db.create_table('censo_transmissiontype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('censo', ['TransmissionType'])

        # Adding model 'VehicleCheckupStatus'
        db.create_table('censo_vehiclecheckupstatus', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('censo', ['VehicleCheckupStatus'])

        # Adding model 'MotorType'
        db.create_table('censo_motortype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('censo', ['MotorType'])

        # Adding model 'IncorporationStatus'
        db.create_table('censo_incorporationstatus', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('censo', ['IncorporationStatus'])

        # Adding model 'VehicleProcedence'
        db.create_table('censo_vehicleprocedence', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('censo', ['VehicleProcedence'])

        # Adding model 'Condition'
        db.create_table('censo_condition', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('censo', ['Condition'])

        # Adding field 'CuerpoMayorMaterialData.picture_front_view'
        db.add_column('censo_cuerpomayormaterialdata', 'picture_front_view', self.gf('sorl.thumbnail.fields.ImageField')(default=0, max_length=100), keep_default=False)

        # Adding field 'CuerpoMayorMaterialData.motor_change_new_manufacturer'
        db.add_column('censo_cuerpomayormaterialdata', 'motor_change_new_manufacturer', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'CuerpoMayorMaterialData.horometraje'
        db.add_column('censo_cuerpomayormaterialdata', 'horometraje', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'CuerpoMayorMaterialData.kilometraje'
        db.add_column('censo_cuerpomayormaterialdata', 'kilometraje', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'CuerpoMayorMaterialData.previous_owner'
        db.add_column('censo_cuerpomayormaterialdata', 'previous_owner', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'CuerpoMayorMaterialData.motor_change_new_number'
        db.add_column('censo_cuerpomayormaterialdata', 'motor_change_new_number', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'CuerpoMayorMaterialData.fk_vehicle_registration'
        db.add_column('censo_cuerpomayormaterialdata', 'fk_vehicle_registration', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['censo.VehicleRegistrationStatus'], null=True), keep_default=False)

        # Adding field 'CuerpoMayorMaterialData.fk_vehicle_checkup'
        db.add_column('censo_cuerpomayormaterialdata', 'fk_vehicle_checkup', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['censo.VehicleCheckupStatus'], null=True), keep_default=False)

        # Adding field 'CuerpoMayorMaterialData.fk_incorporation_status'
        db.add_column('censo_cuerpomayormaterialdata', 'fk_incorporation_status', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['censo.IncorporationStatus'], null=True), keep_default=False)

        # Adding field 'CuerpoMayorMaterialData.antenna_model'
        db.add_column('censo_cuerpomayormaterialdata', 'antenna_model', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'CuerpoMayorMaterialData.portable_radio_equipment_model'
        db.add_column('censo_cuerpomayormaterialdata', 'portable_radio_equipment_model', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'CuerpoMayorMaterialData.fk_procedence'
        db.add_column('censo_cuerpomayormaterialdata', 'fk_procedence', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['censo.VehicleProcedence'], null=True), keep_default=False)

        # Adding field 'CuerpoMayorMaterialData.fire_engine_other_model'
        db.add_column('censo_cuerpomayormaterialdata', 'fire_engine_other_model', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'CuerpoMayorMaterialData.gearbox_repairs'
        db.add_column('censo_cuerpomayormaterialdata', 'gearbox_repairs', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True), keep_default=False)

        # Adding field 'CuerpoMayorMaterialData.portable_radio_equipment_quantity'
        db.add_column('censo_cuerpomayormaterialdata', 'portable_radio_equipment_quantity', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'CuerpoMayorMaterialData.truck_radio_equipment_power'
        db.add_column('censo_cuerpomayormaterialdata', 'truck_radio_equipment_power', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'CuerpoMayorMaterialData.fk_fire_engine_camiva_model'
        db.add_column('censo_cuerpomayormaterialdata', 'fk_fire_engine_camiva_model', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['censo.FireEngineCamivaModel'], null=True), keep_default=False)

        # Adding field 'CuerpoMayorMaterialData.fk_color'
        db.add_column('censo_cuerpomayormaterialdata', 'fk_color', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['censo.Color'], null=True), keep_default=False)

        # Adding field 'CuerpoMayorMaterialData.gearbox_change_new_model'
        db.add_column('censo_cuerpomayormaterialdata', 'gearbox_change_new_model', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'CuerpoMayorMaterialData.last_oil_change_date'
        db.add_column('censo_cuerpomayormaterialdata', 'last_oil_change_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True), keep_default=False)

        # Adding field 'CuerpoMayorMaterialData.service_incorporation_date'
        db.add_column('censo_cuerpomayormaterialdata', 'service_incorporation_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True), keep_default=False)

        # Adding field 'CuerpoMayorMaterialData.observations'
        db.add_column('censo_cuerpomayormaterialdata', 'observations', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'CuerpoMayorMaterialData.vehicle_year'
        db.add_column('censo_cuerpomayormaterialdata', 'vehicle_year', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'CuerpoMayorMaterialData.chassis_number'
        db.add_column('censo_cuerpomayormaterialdata', 'chassis_number', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'CuerpoMayorMaterialData.oil_change_kilometraje'
        db.add_column('censo_cuerpomayormaterialdata', 'oil_change_kilometraje', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'CuerpoMayorMaterialData.antenna_decibels'
        db.add_column('censo_cuerpomayormaterialdata', 'antenna_decibels', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'CuerpoMayorMaterialData.motor_number'
        db.add_column('censo_cuerpomayormaterialdata', 'motor_number', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'CuerpoMayorMaterialData.registered'
        db.add_column('censo_cuerpomayormaterialdata', 'registered', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True), keep_default=False)

        # Adding field 'CuerpoMayorMaterialData.fire_engine_other_manufacturer'
        db.add_column('censo_cuerpomayormaterialdata', 'fire_engine_other_manufacturer', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'CuerpoMayorMaterialData.truck_radio_equipment_manufacturer'
        db.add_column('censo_cuerpomayormaterialdata', 'truck_radio_equipment_manufacturer', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'CuerpoMayorMaterialData.fk_transmission_type'
        db.add_column('censo_cuerpomayormaterialdata', 'fk_transmission_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['censo.TransmissionType'], null=True), keep_default=False)

        # Adding field 'CuerpoMayorMaterialData.antenna_quantity'
        db.add_column('censo_cuerpomayormaterialdata', 'antenna_quantity', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'CuerpoMayorMaterialData.truck_radio_equipment_quantity'
        db.add_column('censo_cuerpomayormaterialdata', 'truck_radio_equipment_quantity', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'CuerpoMayorMaterialData.licence_plate'
        db.add_column('censo_cuerpomayormaterialdata', 'licence_plate', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'CuerpoMayorMaterialData.motor_change_new_model'
        db.add_column('censo_cuerpomayormaterialdata', 'motor_change_new_model', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'CuerpoMayorMaterialData.picture_back_view'
        db.add_column('censo_cuerpomayormaterialdata', 'picture_back_view', self.gf('sorl.thumbnail.fields.ImageField')(default=0, max_length=100), keep_default=False)

        # Adding field 'CuerpoMayorMaterialData.gearbox_change_new_manufacturer'
        db.add_column('censo_cuerpomayormaterialdata', 'gearbox_change_new_manufacturer', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'CuerpoMayorMaterialData.chassis_or_truck_manufacturer'
        db.add_column('censo_cuerpomayormaterialdata', 'chassis_or_truck_manufacturer', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'CuerpoMayorMaterialData.motor_repairs'
        db.add_column('censo_cuerpomayormaterialdata', 'motor_repairs', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True), keep_default=False)

        # Adding field 'CuerpoMayorMaterialData.carrosado_manufacturer'
        db.add_column('censo_cuerpomayormaterialdata', 'carrosado_manufacturer', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'CuerpoMayorMaterialData.picture_side_view'
        db.add_column('censo_cuerpomayormaterialdata', 'picture_side_view', self.gf('sorl.thumbnail.fields.ImageField')(default=0, max_length=100), keep_default=False)

        # Adding field 'CuerpoMayorMaterialData.portable_radio_equipment_manufacturer'
        db.add_column('censo_cuerpomayormaterialdata', 'portable_radio_equipment_manufacturer', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'CuerpoMayorMaterialData.antenna_manufacturer'
        db.add_column('censo_cuerpomayormaterialdata', 'antenna_manufacturer', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'CuerpoMayorMaterialData.truck_radio_equipment_model'
        db.add_column('censo_cuerpomayormaterialdata', 'truck_radio_equipment_model', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'CuerpoMayorMaterialData.model'
        db.add_column('censo_cuerpomayormaterialdata', 'model', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'CuerpoMayorMaterialData.motor_type'
        db.add_column('censo_cuerpomayormaterialdata', 'motor_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['censo.MotorType'], null=True), keep_default=False)

        # Adding field 'CuerpoMayorMaterialData.fk_condition'
        db.add_column('censo_cuerpomayormaterialdata', 'fk_condition', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['censo.Condition'], null=True), keep_default=False)
    
    
    def backwards(self, orm):
        
        # Deleting model 'Color'
        db.delete_table('censo_color')

        # Deleting model 'FireEngineCamivaModel'
        db.delete_table('censo_fireenginecamivamodel')

        # Deleting model 'VehicleRegistrationStatus'
        db.delete_table('censo_vehicleregistrationstatus')

        # Deleting model 'TransmissionType'
        db.delete_table('censo_transmissiontype')

        # Deleting model 'VehicleCheckupStatus'
        db.delete_table('censo_vehiclecheckupstatus')

        # Deleting model 'MotorType'
        db.delete_table('censo_motortype')

        # Deleting model 'IncorporationStatus'
        db.delete_table('censo_incorporationstatus')

        # Deleting model 'VehicleProcedence'
        db.delete_table('censo_vehicleprocedence')

        # Deleting model 'Condition'
        db.delete_table('censo_condition')

        # Deleting field 'CuerpoMayorMaterialData.picture_front_view'
        db.delete_column('censo_cuerpomayormaterialdata', 'picture_front_view')

        # Deleting field 'CuerpoMayorMaterialData.motor_change_new_manufacturer'
        db.delete_column('censo_cuerpomayormaterialdata', 'motor_change_new_manufacturer')

        # Deleting field 'CuerpoMayorMaterialData.horometraje'
        db.delete_column('censo_cuerpomayormaterialdata', 'horometraje')

        # Deleting field 'CuerpoMayorMaterialData.kilometraje'
        db.delete_column('censo_cuerpomayormaterialdata', 'kilometraje')

        # Deleting field 'CuerpoMayorMaterialData.previous_owner'
        db.delete_column('censo_cuerpomayormaterialdata', 'previous_owner')

        # Deleting field 'CuerpoMayorMaterialData.motor_change_new_number'
        db.delete_column('censo_cuerpomayormaterialdata', 'motor_change_new_number')

        # Deleting field 'CuerpoMayorMaterialData.fk_vehicle_registration'
        db.delete_column('censo_cuerpomayormaterialdata', 'fk_vehicle_registration_id')

        # Deleting field 'CuerpoMayorMaterialData.fk_vehicle_checkup'
        db.delete_column('censo_cuerpomayormaterialdata', 'fk_vehicle_checkup_id')

        # Deleting field 'CuerpoMayorMaterialData.fk_incorporation_status'
        db.delete_column('censo_cuerpomayormaterialdata', 'fk_incorporation_status_id')

        # Deleting field 'CuerpoMayorMaterialData.antenna_model'
        db.delete_column('censo_cuerpomayormaterialdata', 'antenna_model')

        # Deleting field 'CuerpoMayorMaterialData.portable_radio_equipment_model'
        db.delete_column('censo_cuerpomayormaterialdata', 'portable_radio_equipment_model')

        # Deleting field 'CuerpoMayorMaterialData.fk_procedence'
        db.delete_column('censo_cuerpomayormaterialdata', 'fk_procedence_id')

        # Deleting field 'CuerpoMayorMaterialData.fire_engine_other_model'
        db.delete_column('censo_cuerpomayormaterialdata', 'fire_engine_other_model')

        # Deleting field 'CuerpoMayorMaterialData.gearbox_repairs'
        db.delete_column('censo_cuerpomayormaterialdata', 'gearbox_repairs')

        # Deleting field 'CuerpoMayorMaterialData.portable_radio_equipment_quantity'
        db.delete_column('censo_cuerpomayormaterialdata', 'portable_radio_equipment_quantity')

        # Deleting field 'CuerpoMayorMaterialData.truck_radio_equipment_power'
        db.delete_column('censo_cuerpomayormaterialdata', 'truck_radio_equipment_power')

        # Deleting field 'CuerpoMayorMaterialData.fk_fire_engine_camiva_model'
        db.delete_column('censo_cuerpomayormaterialdata', 'fk_fire_engine_camiva_model_id')

        # Deleting field 'CuerpoMayorMaterialData.fk_color'
        db.delete_column('censo_cuerpomayormaterialdata', 'fk_color_id')

        # Deleting field 'CuerpoMayorMaterialData.gearbox_change_new_model'
        db.delete_column('censo_cuerpomayormaterialdata', 'gearbox_change_new_model')

        # Deleting field 'CuerpoMayorMaterialData.last_oil_change_date'
        db.delete_column('censo_cuerpomayormaterialdata', 'last_oil_change_date')

        # Deleting field 'CuerpoMayorMaterialData.service_incorporation_date'
        db.delete_column('censo_cuerpomayormaterialdata', 'service_incorporation_date')

        # Deleting field 'CuerpoMayorMaterialData.observations'
        db.delete_column('censo_cuerpomayormaterialdata', 'observations')

        # Deleting field 'CuerpoMayorMaterialData.vehicle_year'
        db.delete_column('censo_cuerpomayormaterialdata', 'vehicle_year')

        # Deleting field 'CuerpoMayorMaterialData.chassis_number'
        db.delete_column('censo_cuerpomayormaterialdata', 'chassis_number')

        # Deleting field 'CuerpoMayorMaterialData.oil_change_kilometraje'
        db.delete_column('censo_cuerpomayormaterialdata', 'oil_change_kilometraje')

        # Deleting field 'CuerpoMayorMaterialData.antenna_decibels'
        db.delete_column('censo_cuerpomayormaterialdata', 'antenna_decibels')

        # Deleting field 'CuerpoMayorMaterialData.motor_number'
        db.delete_column('censo_cuerpomayormaterialdata', 'motor_number')

        # Deleting field 'CuerpoMayorMaterialData.registered'
        db.delete_column('censo_cuerpomayormaterialdata', 'registered')

        # Deleting field 'CuerpoMayorMaterialData.fire_engine_other_manufacturer'
        db.delete_column('censo_cuerpomayormaterialdata', 'fire_engine_other_manufacturer')

        # Deleting field 'CuerpoMayorMaterialData.truck_radio_equipment_manufacturer'
        db.delete_column('censo_cuerpomayormaterialdata', 'truck_radio_equipment_manufacturer')

        # Deleting field 'CuerpoMayorMaterialData.fk_transmission_type'
        db.delete_column('censo_cuerpomayormaterialdata', 'fk_transmission_type_id')

        # Deleting field 'CuerpoMayorMaterialData.antenna_quantity'
        db.delete_column('censo_cuerpomayormaterialdata', 'antenna_quantity')

        # Deleting field 'CuerpoMayorMaterialData.truck_radio_equipment_quantity'
        db.delete_column('censo_cuerpomayormaterialdata', 'truck_radio_equipment_quantity')

        # Deleting field 'CuerpoMayorMaterialData.licence_plate'
        db.delete_column('censo_cuerpomayormaterialdata', 'licence_plate')

        # Deleting field 'CuerpoMayorMaterialData.motor_change_new_model'
        db.delete_column('censo_cuerpomayormaterialdata', 'motor_change_new_model')

        # Deleting field 'CuerpoMayorMaterialData.picture_back_view'
        db.delete_column('censo_cuerpomayormaterialdata', 'picture_back_view')

        # Deleting field 'CuerpoMayorMaterialData.gearbox_change_new_manufacturer'
        db.delete_column('censo_cuerpomayormaterialdata', 'gearbox_change_new_manufacturer')

        # Deleting field 'CuerpoMayorMaterialData.chassis_or_truck_manufacturer'
        db.delete_column('censo_cuerpomayormaterialdata', 'chassis_or_truck_manufacturer')

        # Deleting field 'CuerpoMayorMaterialData.motor_repairs'
        db.delete_column('censo_cuerpomayormaterialdata', 'motor_repairs')

        # Deleting field 'CuerpoMayorMaterialData.carrosado_manufacturer'
        db.delete_column('censo_cuerpomayormaterialdata', 'carrosado_manufacturer')

        # Deleting field 'CuerpoMayorMaterialData.picture_side_view'
        db.delete_column('censo_cuerpomayormaterialdata', 'picture_side_view')

        # Deleting field 'CuerpoMayorMaterialData.portable_radio_equipment_manufacturer'
        db.delete_column('censo_cuerpomayormaterialdata', 'portable_radio_equipment_manufacturer')

        # Deleting field 'CuerpoMayorMaterialData.antenna_manufacturer'
        db.delete_column('censo_cuerpomayormaterialdata', 'antenna_manufacturer')

        # Deleting field 'CuerpoMayorMaterialData.truck_radio_equipment_model'
        db.delete_column('censo_cuerpomayormaterialdata', 'truck_radio_equipment_model')

        # Deleting field 'CuerpoMayorMaterialData.model'
        db.delete_column('censo_cuerpomayormaterialdata', 'model')

        # Deleting field 'CuerpoMayorMaterialData.motor_type'
        db.delete_column('censo_cuerpomayormaterialdata', 'motor_type_id')

        # Deleting field 'CuerpoMayorMaterialData.fk_condition'
        db.delete_column('censo_cuerpomayormaterialdata', 'fk_condition_id')
    
    
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
        'censo.antennaequipment': {
            'Meta': {'object_name': 'AntennaEquipment'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'minor_material_company': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.MinorMaterialCompanyData']", 'null': 'True', 'blank': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'power': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'censo.baseradioequipment': {
            'Meta': {'object_name': 'BaseRadioEquipment'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'minor_material_company': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.MinorMaterialCompanyData']", 'null': 'True', 'blank': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'power': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'censo.buildingmaterialtype': {
            'Meta': {'object_name': 'BuildingMaterialType'},
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
            'province': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.Province']"}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'censo.company': {
            'Meta': {'object_name': 'Company'},
            'address': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'alarm_central': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'assistant_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'captain_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'commune': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['censo.Commune']"}),
            'communes': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['censo.Commune']", 'null': 'True', 'blank': 'True'}),
            'cuerpo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cuerpo_company'", 'to': "orm['censo.Cuerpo']"}),
            'director_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'foundation_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lemma': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'lieutenant_1_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'lieutenant_2_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'lieutenant_3_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'lieutenant_4_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail': ('django.db.models.fields.EmailField', [], {'default': "''", 'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'old_id': ('django.db.models.fields.IntegerField', [], {}),
            'phone': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'postal_box': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'secretary_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'tesorero_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'})
        },
        'censo.companyotherofficial': {
            'Meta': {'object_name': 'CompanyOtherOfficial'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.Company']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'role_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'censo.condition': {
            'Meta': {'object_name': 'Condition'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'censo.cuerpo': {
            'Meta': {'object_name': 'Cuerpo'},
            'address': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'alarm_central_phone': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'commune': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['censo.Commune']"}),
            'communes': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['censo.Commune']", 'null': 'True', 'blank': 'True'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'company_cuerpo'", 'null': 'True', 'to': "orm['censo.Company']"}),
            'cuer_npers_juri': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'decree_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'foundation_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lemma': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'mail': ('django.db.models.fields.EmailField', [], {'default': "''", 'max_length': '75'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'old_id': ('django.db.models.fields.IntegerField', [], {}),
            'phone': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'postal_box': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'rut': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'})
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
            'fk_property_title_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.PropertyTitleType']", 'null': 'True'}),
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
            'property_commodatum_end_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rol_sii': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'secondary_street_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'storage': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'supervisor_office': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'terrain_machine_room_m2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'terrain_session_room_m2': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'})
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
            'cuerpo': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['censo.Cuerpo']", 'unique': 'True', 'blank': 'True'}),
            'denomination': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'fire_engine_other_manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'fire_engine_other_model': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'fk_color': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.Color']", 'null': 'True'}),
            'fk_condition': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.Condition']", 'null': 'True'}),
            'fk_fire_engine_camiva_model': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.FireEngineCamivaModel']", 'null': 'True'}),
            'fk_incorporation_status': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.IncorporationStatus']", 'null': 'True'}),
            'fk_procedence': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.VehicleProcedence']", 'null': 'True'}),
            'fk_transmission_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.TransmissionType']", 'null': 'True'}),
            'fk_vehicle_checkup': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.VehicleCheckupStatus']", 'null': 'True'}),
            'fk_vehicle_registration': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.VehicleRegistrationStatus']", 'null': 'True'}),
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
            'motor_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.MotorType']", 'null': 'True'}),
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
            'picture_back_view': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'picture_front_view': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'picture_general_view': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'picture_internal_distribution_view': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'picture_machine_room_view': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'picture_office_view': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
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
            'cascade_bycar_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cascade_cylinder_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cascade_fixed_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'chainsaw_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'company': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['censo.Company']", 'unique': 'True', 'blank': 'True'}),
            'containers_proteinconcentrate_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'containers_syntheticconcentrate_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'defibrillator_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'electricgenerator_fixed_in_barracks_potency': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'electricgenerator_fixed_in_barracks_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'electricgenerator_fixed_in_car_potency': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'electricgenerator_fixed_in_car_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'electricgenerator_portable_potency': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'electricgenerator_portable_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fensy_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fireman_shoes_company_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fireman_shoes_volunteer_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'firesfans_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
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
        'censo.occupation': {
            'Meta': {'object_name': 'Occupation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'})
        },
        'censo.portableradioequipment': {
            'Meta': {'object_name': 'PortableRadioEquipment'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'minor_material_company': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.MinorMaterialCompanyData']", 'null': 'True', 'blank': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'censo.portadacuerpodata': {
            'Meta': {'object_name': 'PortadaCuerpoData'},
            'cuerpo': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['censo.Cuerpo']", 'unique': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'observations': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
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
            'capital': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.Commune']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'number': ('django.db.models.fields.IntegerField', [], {})
        },
        'censo.role': {
            'Meta': {'object_name': 'Role'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'old_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'})
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
        'censo.userhasrole': {
            'Meta': {'object_name': 'UserHasRole'},
            'cuerpo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.Cuerpo']", 'null': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.UserProfile']"}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.Role']"}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        'censo.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'address': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'cell_phone': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '40'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.Company']", 'null': 'True', 'blank': 'True'}),
            'current_role': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['censo.Role']"}),
            'first_last_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '40'}),
            'first_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'occupation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.Occupation']", 'null': 'True', 'blank': 'True'}),
            'old_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'phone': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '40'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.Region']", 'null': 'True', 'blank': 'True'}),
            'roles': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['censo.Role']", 'through': "orm['censo.UserHasRole']", 'symmetrical': 'False'}),
            'rut': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'second_last_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '40'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'work_address': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'work_phone': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '40'})
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
