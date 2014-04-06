# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Order.doc_file'
        db.add_column(u'orderform_order', 'doc_file',
                      self.gf('django.db.models.fields.files.FileField')(default='doc_file', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Order.doc_file'
        db.delete_column(u'orderform_order', 'doc_file')


    models = {
        u'orderform.order': {
            'Meta': {'object_name': 'Order'},
            'contact': ('django.db.models.fields.CharField', [], {'max_length': '240'}),
            'doc_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '240'})
        }
    }

    complete_apps = ['orderform']