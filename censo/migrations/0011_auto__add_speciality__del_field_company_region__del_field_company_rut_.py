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

        # Deleting field 'Company.region'
        db.delete_column('censo_company', 'region_id')

        # Deleting field 'Company.rut'
        db.delete_column('censo_company', 'rut')

        # Adding field 'Company.website'
        db.add_column('censo_company', 'website', self.gf('django.db.models.fields.CharField')(default='', max_length=255), keep_default=False)

        # Adding field 'Company.commune'
        db.add_column('censo_company', 'commune', self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='+', to=orm['censo.Commune']), keep_default=False)

        # Adding field 'Company.fax'
        db.add_column('censo_company', 'fax', self.gf('django.db.models.fields.CharField')(default='', max_length=255), keep_default=False)

        # Adding field 'Company.lemma'
        db.add_column('censo_company', 'lemma', self.gf('django.db.models.fields.CharField')(default='', max_length=255), keep_default=False)

        # Adding field 'Company.postal_box'
        db.add_column('censo_company', 'postal_box', self.gf('django.db.models.fields.CharField')(default='', max_length=255), keep_default=False)

        # Adding field 'Company.number'
        db.add_column('censo_company', 'number', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'Company.phone'
        db.add_column('censo_company', 'phone', self.gf('django.db.models.fields.CharField')(default='', max_length=255), keep_default=False)

        # Adding field 'Company.address'
        db.add_column('censo_company', 'address', self.gf('django.db.models.fields.EmailField')(default='', max_length=255), keep_default=False)

        # Adding field 'Company.mail'
        db.add_column('censo_company', 'mail', self.gf('django.db.models.fields.EmailField')(default='', max_length=255), keep_default=False)

        # Adding field 'Company.alarm_central'
        db.add_column('censo_company', 'alarm_central', self.gf('django.db.models.fields.CharField')(default='', max_length=255), keep_default=False)

        # Adding field 'Company.foundation_date'
        db.add_column('censo_company', 'foundation_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True), keep_default=False)

        # Adding M2M table for field communes on 'Company'
        db.create_table('censo_company_communes', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('company', models.ForeignKey(orm['censo.company'], null=False)),
            ('commune', models.ForeignKey(orm['censo.commune'], null=False))
        ))
        db.create_unique('censo_company_communes', ['company_id', 'commune_id'])

        # Adding M2M table for field specialities on 'Company'
        db.create_table('censo_company_specialities', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('company', models.ForeignKey(orm['censo.company'], null=False)),
            ('speciality', models.ForeignKey(orm['censo.speciality'], null=False))
        ))
        db.create_unique('censo_company_specialities', ['company_id', 'speciality_id'])

        # Changing field 'Company.name'
        db.alter_column('censo_company', 'name', self.gf('django.db.models.fields.CharField')(max_length=255))
    
    
    def backwards(self, orm):
        
        # Deleting model 'Speciality'
        db.delete_table('censo_speciality')

        # Adding field 'Company.region'
        db.add_column('censo_company', 'region', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['censo.Region']), keep_default=False)

        # Adding field 'Company.rut'
        db.add_column('censo_company', 'rut', self.gf('django.db.models.fields.CharField')(default='', max_length=10), keep_default=False)

        # Deleting field 'Company.website'
        db.delete_column('censo_company', 'website')

        # Deleting field 'Company.commune'
        db.delete_column('censo_company', 'commune_id')

        # Deleting field 'Company.fax'
        db.delete_column('censo_company', 'fax')

        # Deleting field 'Company.lemma'
        db.delete_column('censo_company', 'lemma')

        # Deleting field 'Company.postal_box'
        db.delete_column('censo_company', 'postal_box')

        # Deleting field 'Company.number'
        db.delete_column('censo_company', 'number')

        # Deleting field 'Company.phone'
        db.delete_column('censo_company', 'phone')

        # Deleting field 'Company.address'
        db.delete_column('censo_company', 'address')

        # Deleting field 'Company.mail'
        db.delete_column('censo_company', 'mail')

        # Deleting field 'Company.alarm_central'
        db.delete_column('censo_company', 'alarm_central')

        # Deleting field 'Company.foundation_date'
        db.delete_column('censo_company', 'foundation_date')

        # Removing M2M table for field communes on 'Company'
        db.delete_table('censo_company_communes')

        # Removing M2M table for field specialities on 'Company'
        db.delete_table('censo_company_specialities')

        # Changing field 'Company.name'
        db.alter_column('censo_company', 'name', self.gf('django.db.models.fields.CharField')(max_length=100))
    
    
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
            'address': ('django.db.models.fields.EmailField', [], {'default': "''", 'max_length': '255'}),
            'alarm_central': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'commune': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['censo.Commune']"}),
            'communes': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['censo.Commune']", 'null': 'True', 'blank': 'True'}),
            'cuerpo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cuerpo_company'", 'to': "orm['censo.Cuerpo']"}),
            'fax': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'foundation_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lemma': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'mail': ('django.db.models.fields.EmailField', [], {'default': "''", 'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
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
            'phone': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'postal_box': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'rut': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'})
        },
        'censo.occupation': {
            'Meta': {'object_name': 'Occupation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'})
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
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'})
        },
        'censo.speciality': {
            'Meta': {'object_name': 'Speciality'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'censo.userhasrole': {
            'Meta': {'object_name': 'UserHasRole'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.UserProfile']"}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.Role']"})
        },
        'censo.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'address': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'cell_phone': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '40'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.Company']"}),
            'first_last_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '40'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'occupation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.Occupation']"}),
            'phone': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '40'}),
            'roles': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['censo.Role']", 'through': "orm['censo.UserHasRole']", 'symmetrical': 'False'}),
            'rut': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'second_last_lane': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '40'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'work_address': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'work_phone': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '40'})
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
