# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Glossary'
        db.create_table('glossary_glossary', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
        ))
        db.send_create_signal('glossary', ['Glossary'])

        # Adding model 'Term'
        db.create_table('glossary_term', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('glossary', self.gf('django.db.models.fields.related.ForeignKey')(related_name='terms', to=orm['glossary.Glossary'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('definition', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('glossary', ['Term'])


    def backwards(self, orm):
        
        # Deleting model 'Glossary'
        db.delete_table('glossary_glossary')

        # Deleting model 'Term'
        db.delete_table('glossary_term')


    models = {
        'glossary.glossary': {
            'Meta': {'object_name': 'Glossary'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'glossary.term': {
            'Meta': {'object_name': 'Term'},
            'definition': ('django.db.models.fields.TextField', [], {}),
            'glossary': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'terms'", 'to': "orm['glossary.Glossary']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['glossary']
