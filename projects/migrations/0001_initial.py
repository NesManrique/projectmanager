# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Project'
        db.create_table(u'projects_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creado', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modificado', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('cliente', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('verticales', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('inicio', self.gf('django.db.models.fields.DateTimeField')()),
            ('fin', self.gf('django.db.models.fields.DateTimeField')()),
            ('horas_asig', self.gf('django.db.models.fields.IntegerField')()),
            ('horas_sem', self.gf('django.db.models.fields.IntegerField')()),
            ('horas_acum', self.gf('django.db.models.fields.IntegerField')()),
            ('horas_totales', self.gf('django.db.models.fields.IntegerField')()),
            ('status', self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True)),
            ('detalle', self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True)),
            ('consultores', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('lider', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'projects', ['Project'])

        # Adding model 'Update'
        db.create_table(u'projects_update', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('proyecto', self.gf('django.db.models.fields.related.ForeignKey')(related_name='actualizacion', to=orm['projects.Project'])),
            ('creado', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modificado', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('fecha_detalle', self.gf('django.db.models.fields.DateTimeField')()),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'projects', ['Update'])


    def backwards(self, orm):
        # Deleting model 'Project'
        db.delete_table(u'projects_project')

        # Deleting model 'Update'
        db.delete_table(u'projects_update')


    models = {
        u'projects.project': {
            'Meta': {'ordering': "('cliente', 'titulo')", 'object_name': 'Project'},
            'cliente': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'consultores': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'creado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'detalle': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'fin': ('django.db.models.fields.DateTimeField', [], {}),
            'horas_acum': ('django.db.models.fields.IntegerField', [], {}),
            'horas_asig': ('django.db.models.fields.IntegerField', [], {}),
            'horas_sem': ('django.db.models.fields.IntegerField', [], {}),
            'horas_totales': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inicio': ('django.db.models.fields.DateTimeField', [], {}),
            'lider': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'modificado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'verticales': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'projects.update': {
            'Meta': {'object_name': 'Update'},
            'creado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'fecha_detalle': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'proyecto': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'actualizacion'", 'to': u"orm['projects.Project']"})
        }
    }

    complete_apps = ['projects']