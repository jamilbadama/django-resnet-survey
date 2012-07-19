# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Survey.is_active'
        db.delete_column('survey_survey', 'is_active')

        # Adding field 'Survey.start_date'
        db.add_column('survey_survey', 'start_date',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now),
                      keep_default=False)

        # Adding field 'Survey.end_date'
        db.add_column('survey_survey', 'end_date',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Survey.is_active'
        db.add_column('survey_survey', 'is_active',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Deleting field 'Survey.start_date'
        db.delete_column('survey_survey', 'start_date')

        # Deleting field 'Survey.end_date'
        db.delete_column('survey_survey', 'end_date')


    models = {
        'survey.answer': {
            'Meta': {'object_name': 'Answer'},
            'ballot': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['survey.Ballot']", 'null': 'True'}),
            'choice': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['survey.Choice']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        'survey.ballot': {
            'Meta': {'object_name': 'Ballot'},
            'datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.GenericIPAddressField', [], {'default': "'127.0.0.1'", 'max_length': '39'}),
            'survey': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['survey.Survey']", 'null': 'True'})
        },
        'survey.choice': {
            'Meta': {'object_name': 'Choice'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['survey.Question']"})
        },
        'survey.question': {
            'Meta': {'object_name': 'Question'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'survey': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['survey.Survey']"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        'survey.survey': {
            'Meta': {'object_name': 'Survey'},
            'end_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '1024', 'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        }
    }

    complete_apps = ['survey']