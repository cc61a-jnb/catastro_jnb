# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Changing field 'Company.address'
        db.alter_column('censo_company', 'address', self.gf('django.db.models.fields.CharField')(max_length=255))
    
    
    def backwards(self, orm):
        
        # Changing field 'Company.address'
        db.alter_column('censo_company', 'address', self.gf('django.db.models.fields.EmailField')(max_length=255))
    
    
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
            'specialities': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['censo.Speciality']", 'null': 'True', 'blank': 'True'}),
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
        'censo.occupation': {
            'Meta': {'object_name': 'Occupation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'})
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
            'has_internet': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internet_provider': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'notebooks_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'observations': ('django.db.models.fields.TextField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'printers_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'projectors_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'social_facebook_account_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'social_other_account_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'social_twitter_account_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'volunteer_active_men_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'volunteer_active_women_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'volunteer_age_60_or_more_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'volunteer_age_between_18_25_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'volunteer_age_between_26_30_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'volunteer_age_between_31_35_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'volunteer_age_between_36_40_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'volunteer_age_between_41_45_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'volunteer_age_between_46_50_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'volunteer_age_between_51_55_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'volunteer_age_between_56_60_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'volunteer_antiquity_required_to_be_paid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'volunteer_brigada_juvenil_antiquity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'volunteer_brigada_juvenil_members_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'volunteer_brigada_juvenil_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'volunteer_brigada_juvenil_responsible_email': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'volunteer_brigada_juvenil_responsible_instructor': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'volunteer_class_f_bomberos_driver_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'volunteer_class_f_cuarteleros_driver_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'volunteer_education_basica_complete_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'volunteer_education_media_complete_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'volunteer_education_tecnica_complete_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'volunteer_education_universitaria_complete_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'volunteer_gt_than_3_years_academia_course_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'volunteer_gt_than_3_years_cuerpo_course_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'volunteer_hoja_de_vida_cargo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'volunteer_hoja_de_vida_email': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'volunteer_hoja_de_vida_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'volunteer_hoja_de_vida_phone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'volunteer_lt_than_3_years_academia_course_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'volunteer_lt_than_3_years_cuerpo_course_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'volunteer_paid_men_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'volunteer_paid_women_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'volunteer_total_men_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'volunteer_total_women_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'volunteer_with_work_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
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
