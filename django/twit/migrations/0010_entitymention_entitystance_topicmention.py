# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twit', '0009_auto_20160502_2322'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntityMention',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('doc_char_begin', models.IntegerField()),
                ('doc_char_end', models.IntegerField()),
                ('gloss', models.TextField()),
                ('best_entity', models.TextField()),
                ('tweet', models.ForeignKey(to='twit.Tweet')),
            ],
        ),
        migrations.CreateModel(
            name='EntityStance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('entity', models.TextField(help_text='Entity with stance')),
                ('stance', models.FloatField(help_text='Stance value')),
                ('score', models.FloatField(help_text='Confidence of stance value')),
                ('tweet', models.ForeignKey(to='twit.Tweet')),
            ],
        ),
        migrations.CreateModel(
            name='TopicMention',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('topic', models.TextField(help_text='Description of a topic.')),
                ('score', models.FloatField(help_text='Confidence of class')),
                ('tweet', models.ForeignKey(to='twit.Tweet')),
            ],
        ),
    ]
