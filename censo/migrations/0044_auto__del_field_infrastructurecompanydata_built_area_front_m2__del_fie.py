# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Deleting field 'InfrastructureCompanyData.built_area_front_m2'
        db.delete_column('censo_infrastructurecompanydata', 'built_area_front_m2')

        # Deleting field 'InfrastructureCompanyData.built_area_total_m2'
        db.delete_column('censo_infrastructurecompanydata', 'built_area_total_m2')

        # Deleting field 'InfrastructureCompanyData.built_area_back_m2'
        db.delete_column('censo_infrastructurecompanydata', 'built_area_back_m2')

        # Adding field 'InfrastructureCompanyData.built_meters_surface_m2'
        db.add_column('censo_infrastructurecompanydata', 'built_meters_surface_m2', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'InfrastructureCompanyData.built_meters_total_m2'
        db.add_column('censo_infrastructurecompanydata', 'built_meters_total_m2', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'InfrastructureCompanyData.built_meters_back_m'
        db.add_column('censo_infrastructurecompanydata', 'built_meters_back_m', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'InfrastructureCompanyData.built_meters_front_m'
        db.add_column('censo_infrastructurecompanydata', 'built_meters_front_m', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)
    
    
    def backwards(self, orm):
        
        # Adding field 'InfrastructureCompanyData.built_area_front_m2'
        db.add_column('censo_infrastructurecompanydata', 'built_area_front_m2', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'InfrastructureCompanyData.built_area_total_m2'
        db.add_column('censo_infrastructurecompanydata', 'built_area_total_m2', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'InfrastructureCompanyData.built_area_back_m2'
        db.add_column('censo_infrastructurecompanydata', 'built_area_back_m2', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Deleting field 'InfrastructureCompanyData.built_meters_surface_m2'
        db.delete_column('censo_infrastructurecompanydata', 'built_meters_surface_m2')

        # Deleting field 'InfrastructureCompanyData.built_meters_total_m2'
        db.delete_column('censo_infrastructurecompanydata', 'built_meters_total_m2')

        # Deleting field 'InfrastructureCompanyData.built_meters_back_m'
        db.delete_column('censo_infrastructurecompanydata', 'built_meters_back_m')

        # Deleting field 'InfrastructureCompanyData.built_meters_front_m'
        db.delete_column('censo_infrastructurecompanydata', 'built_meters_front_m')
    
    
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
        'censo.buildingmaterialtype': {
            'Meta': {'object_name': 'BuildingMaterialType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'})
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
            'commune': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['censo.Commune']"}),
            'communes': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['censo.Commune']", 'null': 'True', 'blank': 'True'}),
            'cuerpo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cuerpo_company'", 'to': "orm['censo.Cuerpo']"}),
            'fax': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'foundation_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lemma': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'mail': ('django.db.models.fields.EmailField', [], {'default': "''", 'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'old_id': ('django.db.models.fields.IntegerField', [], {}),
            'phone': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'postal_box': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'website': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'})
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
            'built_meters_back_m': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'built_meters_front_m': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'built_meters_surface_m2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'built_meters_total_m2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cafeteria': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'captain_office': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'common_bathrooms': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'common_offices': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'company': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['censo.Company']", 'unique': 'True', 'blank': 'True'}),
            'director_office': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'fk_property_title_type': ('django.db.models.fields.related.ForeignKey', [], {'default': '6', 'to': "orm['censo.PropertyTitleType']", 'null': 'True'}),
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
            'property_commodatum_end_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
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
        'censo.occupation': {
            'Meta': {'object_name': 'Occupation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'})
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
