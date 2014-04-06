# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Order.sourcelang'
        db.add_column(u'orderform_order', 'sourcelang',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank='true'),
                      keep_default=False)

        # Adding field 'Order.resultlang'
        db.add_column(u'orderform_order', 'resultlang',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank='true'),
                      keep_default=False)

        # Adding field 'Order.comments'
        db.add_column(u'orderform_order', 'comments',
                      self.gf('django.db.models.fields.TextField')(default='', blank='true'),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Order.sourcelang'
        db.delete_column(u'orderform_order', 'sourcelang')

        # Deleting field 'Order.resultlang'
        db.delete_column(u'orderform_order', 'resultlang')

        # Deleting field 'Order.comments'
        db.delete_column(u'orderform_order', 'comments')


    models = {
        u'orderform.order': {
            'Meta': {'object_name': 'Order'},
            'comments': ('django.db.models.fields.TextField', [], {'blank': "'true'"}),
            'contact': ('django.db.models.fields.CharField', [], {'max_length': '240'}),
            'doc_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': "'true'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '240'}),
            'resultlang': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': "'true'"}),
            'sourcelang': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': "'true'"})
        }
    }

    complete_apps = ['orderform']