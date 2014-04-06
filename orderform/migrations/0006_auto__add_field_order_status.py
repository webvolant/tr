# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Order.status'
        db.add_column(u'orderform_order', 'status',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank='true'),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Order.status'
        db.delete_column(u'orderform_order', 'status')


    models = {
        u'orderform.order': {
            'Meta': {'object_name': 'Order'},
            'comments': ('django.db.models.fields.TextField', [], {'blank': "'true'"}),
            'contact': ('django.db.models.fields.CharField', [], {'max_length': '240'}),
            'doc_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': "'true'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '240'}),
            'resultlang': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': "'true'"}),
            'sourcelang': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': "'true'"}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': "'true'"})
        }
    }

    complete_apps = ['orderform']