# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Order.contact'
        db.add_column(u'orderform_order', 'contact',
                      self.gf('django.db.models.fields.CharField')(default='contact', max_length=240),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Order.contact'
        db.delete_column(u'orderform_order', 'contact')


    models = {
        u'orderform.order': {
            'Meta': {'object_name': 'Order'},
            'contact': ('django.db.models.fields.CharField', [], {'max_length': '240'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '240'})
        }
    }

    complete_apps = ['orderform']