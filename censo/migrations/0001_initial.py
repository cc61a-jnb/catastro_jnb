# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Speciality'
        db.create_table('censo_speciality', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('censo', ['Speciality'])

        # Adding model 'Role'
        db.create_table('censo_role', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('old_id', self.gf('django.db.models.fields.IntegerField')(unique=True)),
        ))
        db.send_create_signal('censo', ['Role'])

        # Adding model 'Occupation'
        db.create_table('censo_occupation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
        ))
        db.send_create_signal('censo', ['Occupation'])

        # Adding model 'Commune'
        db.create_table('censo_commune', (
            ('url', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('province', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['censo.Province'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('censo', ['Commune'])

        # Adding model 'Region'
        db.create_table('censo_region', (
            ('capital', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['censo.Commune'], null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('censo', ['Region'])

        # Adding model 'Cuerpo'
        db.create_table('censo_cuerpo', (
            ('commune', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['censo.Commune'])),
            ('fax', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('lemma', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('old_id', self.gf('django.db.models.fields.IntegerField')()),
            ('url', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('decree_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(related_name='company_cuerpo', null=True, to=orm['censo.Company'])),
            ('mail', self.gf('django.db.models.fields.EmailField')(default='', max_length=75)),
            ('phone', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('cuer_npers_juri', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('postal_box', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('alarm_central_phone', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rut', self.gf('django.db.models.fields.CharField')(default='', max_length=10)),
            ('foundation_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('censo', ['Cuerpo'])

        # Adding M2M table for field communes on 'Cuerpo'
        db.create_table('censo_cuerpo_communes', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('cuerpo', models.ForeignKey(orm['censo.cuerpo'], null=False)),
            ('commune', models.ForeignKey(orm['censo.commune'], null=False))
        ))
        db.create_unique('censo_cuerpo_communes', ['cuerpo_id', 'commune_id'])

        # Adding model 'VolunteerData'
        db.create_table('censo_volunteerdata', (
            ('volunteer_age_between_51_55_men_quantity', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('volunteer_hoja_de_vida_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('volunteer_age_between_26_30_men_quantity', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('volunteer_education_universitaria_complete_quantity', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('volunteer_age_60_or_more_men_quantity', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('volunteer_hoja_de_vida_phone', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('volunteer_age_between_46_50_men_quantity', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('volunteer_gt_than_3_years_cuerpo_course_quantity', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('volunteer_brigada_juvenil_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('volunteer_active_women_quantity', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('volunteer_brigada_juvenil_responsible_email', self.gf('django.db.models.fields.EmailField')(max_length=255, null=True, blank=True)),
            ('volunteer_age_between_46_50_women_quantity', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('volunteer_age_between_18_25_women_quantity', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('volunteer_active_men_quantity', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('volunteer_age_between_56_60_women_quantity', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('volunteer_lt_than_3_years_cuerpo_course_quantity', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('volunteer_education_basica_complete_quantity', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('volunteer_brigada_juvenil_responsible_instructor', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('specialities_other', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('volunteer_age_between_31_35_men_quantity', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('volunteer_gt_than_3_years_academia_course_quantity', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('observations', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('volunteer_brigada_juvenil_antiquity', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('volunteer_age_between_31_35_women_quantity', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('notebooks_quantity', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('company', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['censo.Company'], unique=True, blank=True)),
            ('social_twitter_account_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('volunteer_age_between_36_40_women_quantity', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('volunteer_honorary_women_quantity', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('social_facebook_account_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('volunteer_age_between_18_25_men_quantity', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('volunteer_age_between_26_30_women_quantity', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('printers_quantity', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('volunteer_lt_than_3_years_academia_course_quantity', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('volunteer_with_work_quantity', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('volunteer_antiquity_required_to_honorary', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('volunteer_class_f_bomberos_driver_quantity', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('volunteer_education_tecnica_complete_quantity', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('fk_internet_provider', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['censo.InternetProvider'], null=True, blank=True)),
            ('volunteer_age_60_or_more_women_quantity', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('volunteer_hoja_de_vida_cargo', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('volunteer_total_women_quantity', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('volunteer_age_between_51_55_women_quantity', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('volunteer_brigada_juvenil_members_quantity', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('volunteer_education_media_complete_quantity', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('social_other_account_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('volunteer_age_between_41_45_men_quantity', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('volunteer_age_between_36_40_men_quantity', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('volunteer_class_f_cuarteleros_driver_quantity', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('volunteer_total_men_quantity', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('volunteer_age_between_41_45_women_quantity', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('volunteer_age_between_56_60_men_quantity', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('computers_quantity', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('volunteer_honorary_men_quantity', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('projectors_quantity', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('volunteer_hoja_de_vida_email', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('censo', ['VolunteerData'])

        # Adding M2M table for field specialities on 'VolunteerData'
        db.create_table('censo_volunteerdata_specialities', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('volunteerdata', models.ForeignKey(orm['censo.volunteerdata'], null=False)),
            ('speciality', models.ForeignKey(orm['censo.speciality'], null=False))
        ))
        db.create_unique('censo_volunteerdata_specialities', ['volunteerdata_id', 'speciality_id'])

        # Adding model 'Company'
        db.create_table('censo_company', (
            ('website', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('commune', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['censo.Commune'])),
            ('fax', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('lemma', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('old_id', self.gf('django.db.models.fields.IntegerField')()),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
            ('cuerpo', self.gf('django.db.models.fields.related.ForeignKey')(related_name='cuerpo_company', to=orm['censo.Cuerpo'])),
            ('phone', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('postal_box', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('address', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('mail', self.gf('django.db.models.fields.EmailField')(default='', max_length=255)),
            ('alarm_central', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('foundation_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('censo', ['Company'])

        # Adding M2M table for field communes on 'Company'
        db.create_table('censo_company_communes', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('company', models.ForeignKey(orm['censo.company'], null=False)),
            ('commune', models.ForeignKey(orm['censo.commune'], null=False))
        ))
        db.create_unique('censo_company_communes', ['company_id', 'commune_id'])

        # Adding model 'UserProfile'
        db.create_table('censo_userprofile', (
            ('first_name', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('current_role', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['censo.Role'])),
            ('second_last_name', self.gf('django.db.models.fields.CharField')(default='', max_length=40)),
            ('work_phone', self.gf('django.db.models.fields.CharField')(default='', max_length=40)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('first_last_name', self.gf('django.db.models.fields.CharField')(default='', max_length=40)),
            ('old_id', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('phone', self.gf('django.db.models.fields.CharField')(default='', max_length=40)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('work_address', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('address', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['censo.Region'], null=True, blank=True)),
            ('cell_phone', self.gf('django.db.models.fields.CharField')(default='', max_length=40)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['censo.Company'], null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rut', self.gf('django.db.models.fields.CharField')(default='', max_length=10)),
            ('occupation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['censo.Occupation'], null=True, blank=True)),
        ))
        db.send_create_signal('censo', ['UserProfile'])

        # Adding model 'UserHasRole'
        db.create_table('censo_userhasrole', (
            ('profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['censo.UserProfile'])),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('start_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('cuerpo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['censo.Cuerpo'], null=True, blank=True)),
            ('role', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['censo.Role'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('censo', ['UserHasRole'])

        # Adding model 'Province'
        db.create_table('censo_province', (
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['censo.Region'])),
            ('old_id', self.gf('django.db.models.fields.IntegerField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('censo', ['Province'])

        # Adding model 'InternetProvider'
        db.create_table('censo_internetprovider', (
            ('ordering', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('censo', ['InternetProvider'])

        # Adding model 'InfrastructureCompanyData'
        db.create_table('censo_infrastructurecompanydata', (
            ('terrain_machine_room_m2', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('barrack_house_bedroom', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('building_initial_construction_year', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('night_guard_office_women_bathroom', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('women_bathroom', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('men_bathroom', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('fk_property_title_type', self.gf('django.db.models.fields.related.ForeignKey')(default=6, to=orm['censo.PropertyTitleType'], null=True)),
            ('building_initial_construction_legal', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('night_guard_office_women_bathroom_wc', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('secretary_office', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('night_guard_office_women_beds', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('narrow_street_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('night_guard_office_women_bathroom_showers', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('captain_office', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('cafeteria', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('rol_sii', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('building_extension_construction_year', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('night_guard_office_men_bathroom_urinary', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('storage', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('night_guard_office_men_beds', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('main_street_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('inscription_number', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('built_area_front_m2', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('inscription_owner_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('secondary_street_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('night_guard_office_kitchen', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('night_guard_office_men_bathroom_wc', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('inscription_fojas', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('common_bathrooms', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('living_room', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('company', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['censo.Company'], unique=True, blank=True)),
            ('built_area_total_m2', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('inscription_year', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('barrack_house_bathroom', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('night_guard_office_men_bathroom_showers', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('observations', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('others', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('kitchen', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('built_area_back_m2', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('barrack_house_kitchen', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('property_commodatum_end_year', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('night_guard_office_men_bathroom', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('building_extension_construction_legal', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('terrain_session_room_m2', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('director_office', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('officers_office', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('common_offices', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('inscription_real_estate_registrar', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('treasurer_office', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('lieutenant_office', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal('censo', ['InfrastructureCompanyData'])

        # Adding M2M table for field building_material_type on 'InfrastructureCompanyData'
        db.create_table('censo_infrastructurecompanydata_building_material_type', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('infrastructurecompanydata', models.ForeignKey(orm['censo.infrastructurecompanydata'], null=False)),
            ('buildingmaterialtype', models.ForeignKey(orm['censo.buildingmaterialtype'], null=False))
        ))
        db.create_unique('censo_infrastructurecompanydata_building_material_type', ['infrastructurecompanydata_id', 'buildingmaterialtype_id'])

        # Adding model 'BuildingMaterialType'
        db.create_table('censo_buildingmaterialtype', (
            ('ordering', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('censo', ['BuildingMaterialType'])

        # Adding model 'PropertyTitleType'
        db.create_table('censo_propertytitletype', (
            ('ordering', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('censo', ['PropertyTitleType'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'Speciality'
        db.delete_table('censo_speciality')

        # Deleting model 'Role'
        db.delete_table('censo_role')

        # Deleting model 'Occupation'
        db.delete_table('censo_occupation')

        # Deleting model 'Commune'
        db.delete_table('censo_commune')

        # Deleting model 'Region'
        db.delete_table('censo_region')

        # Deleting model 'Cuerpo'
        db.delete_table('censo_cuerpo')

        # Removing M2M table for field communes on 'Cuerpo'
        db.delete_table('censo_cuerpo_communes')

        # Deleting model 'VolunteerData'
        db.delete_table('censo_volunteerdata')

        # Removing M2M table for field specialities on 'VolunteerData'
        db.delete_table('censo_volunteerdata_specialities')

        # Deleting model 'Company'
        db.delete_table('censo_company')

        # Removing M2M table for field communes on 'Company'
        db.delete_table('censo_company_communes')

        # Deleting model 'UserProfile'
        db.delete_table('censo_userprofile')

        # Deleting model 'UserHasRole'
        db.delete_table('censo_userhasrole')

        # Deleting model 'Province'
        db.delete_table('censo_province')

        # Deleting model 'InternetProvider'
        db.delete_table('censo_internetprovider')

        # Deleting model 'InfrastructureCompanyData'
        db.delete_table('censo_infrastructurecompanydata')

        # Removing M2M table for field building_material_type on 'InfrastructureCompanyData'
        db.delete_table('censo_infrastructurecompanydata_building_material_type')

        # Deleting model 'BuildingMaterialType'
        db.delete_table('censo_buildingmaterialtype')

        # Deleting model 'PropertyTitleType'
        db.delete_table('censo_propertytitletype')
    
    
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
            'built_area_back_m2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'built_area_front_m2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'built_area_total_m2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
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
