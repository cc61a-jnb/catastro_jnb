# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Commune'
        db.create_table('censo_commune', (
            ('url', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('province', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['censo.Province'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('censo', ['Commune'])

        # Adding model 'Province'
        db.create_table('censo_province', (
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['censo.Region'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('censo', ['Province'])

        # Adding field 'Region.capital'
        db.add_column('censo_region', 'capital', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['censo.Commune']), keep_default=False)

        # Adding field 'Cuerpo.commune'
        db.add_column('censo_cuerpo', 'commune', self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='+', to=orm['censo.Commune']), keep_default=False)

        # Adding field 'Cuerpo.fax'
        db.add_column('censo_cuerpo', 'fax', self.gf('django.db.models.fields.CharField')(default='', max_length=100), keep_default=False)

        # Adding field 'Cuerpo.lemma'
        db.add_column('censo_cuerpo', 'lemma', self.gf('django.db.models.fields.CharField')(default=0, max_length=255), keep_default=False)

        # Adding field 'Cuerpo.postal_box'
        db.add_column('censo_cuerpo', 'postal_box', self.gf('django.db.models.fields.CharField')(default='', max_length=100), keep_default=False)

        # Adding field 'Cuerpo.url'
        db.add_column('censo_cuerpo', 'url', self.gf('django.db.models.fields.CharField')(default='', max_length=255), keep_default=False)

        # Adding field 'Cuerpo.company'
        db.add_column('censo_cuerpo', 'company', self.gf('django.db.models.fields.related.ForeignKey')(related_name='company_cuerpo', null=True, to=orm['censo.Company']), keep_default=False)

        # Adding field 'Cuerpo.decree_date'
        db.add_column('censo_cuerpo', 'decree_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True), keep_default=False)

        # Adding field 'Cuerpo.phone'
        db.add_column('censo_cuerpo', 'phone', self.gf('django.db.models.fields.CharField')(default='', max_length=100), keep_default=False)

        # Adding field 'Cuerpo.address'
        db.add_column('censo_cuerpo', 'address', self.gf('django.db.models.fields.CharField')(default='', max_length=255), keep_default=False)

        # Adding field 'Cuerpo.mail'
        db.add_column('censo_cuerpo', 'mail', self.gf('django.db.models.fields.EmailField')(default='', max_length=75), keep_default=False)

        # Adding field 'Cuerpo.alarm_central_phone'
        db.add_column('censo_cuerpo', 'alarm_central_phone', self.gf('django.db.models.fields.CharField')(default=0, max_length=100), keep_default=False)

        # Adding field 'Cuerpo.foundation_date'
        db.add_column('censo_cuerpo', 'foundation_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True), keep_default=False)

        # Adding M2M table for field communes on 'Cuerpo'
        db.create_table('censo_cuerpo_communes', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('cuerpo', models.ForeignKey(orm['censo.cuerpo'], null=False)),
            ('commune', models.ForeignKey(orm['censo.commune'], null=False))
        ))
        db.create_unique('censo_cuerpo_communes', ['cuerpo_id', 'commune_id'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'Commune'
        db.delete_table('censo_commune')

        # Deleting model 'Province'
        db.delete_table('censo_province')

        # Deleting field 'Region.capital'
        db.delete_column('censo_region', 'capital_id')

        # Deleting field 'Cuerpo.commune'
        db.delete_column('censo_cuerpo', 'commune_id')

        # Deleting field 'Cuerpo.fax'
        db.delete_column('censo_cuerpo', 'fax')

        # Deleting field 'Cuerpo.lemma'
        db.delete_column('censo_cuerpo', 'lemma')

        # Deleting field 'Cuerpo.postal_box'
        db.delete_column('censo_cuerpo', 'postal_box')

        # Deleting field 'Cuerpo.url'
        db.delete_column('censo_cuerpo', 'url')

        # Deleting field 'Cuerpo.company'
        db.delete_column('censo_cuerpo', 'company_id')

        # Deleting field 'Cuerpo.decree_date'
        db.delete_column('censo_cuerpo', 'decree_date')

        # Deleting field 'Cuerpo.phone'
        db.delete_column('censo_cuerpo', 'phone')

        # Deleting field 'Cuerpo.address'
        db.delete_column('censo_cuerpo', 'address')

        # Deleting field 'Cuerpo.mail'
        db.delete_column('censo_cuerpo', 'mail')

        # Deleting field 'Cuerpo.alarm_central_phone'
        db.delete_column('censo_cuerpo', 'alarm_central_phone')

        # Deleting field 'Cuerpo.foundation_date'
        db.delete_column('censo_cuerpo', 'foundation_date')

        # Removing M2M table for field communes on 'Cuerpo'
        db.delete_table('censo_cuerpo_communes')
    
    
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
            'cuerpo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cuerpo_company'", 'to': "orm['censo.Cuerpo']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.Region']"}),
            'rut': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'})
        },
        'censo.cuerpo': {
            'Meta': {'object_name': 'Cuerpo'},
            'address': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'alarm_central_phone': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'commune': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['censo.Commune']"}),
            'communes': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['censo.Commune']", 'null': 'True', 'blank': 'True'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'company_cuerpo'", 'null': 'True', 'to': "orm['censo.Company']"}),
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
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.Region']"})
        },
        'censo.region': {
            'Meta': {'object_name': 'Region'},
            'capital': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['censo.Commune']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'number': ('django.db.models.fields.IntegerField', [], {})
        },
        'censo.role': {
            'Meta': {'object_name': 'Role'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'})
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
