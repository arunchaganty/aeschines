# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('javanlp', '0002_auto_20151105_2216'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.TextField(help_text='Name of the speaking event')),
                ('date', models.DateField(help_text='When was the event?')),
            ],
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.TextField(help_text='Name of candidate')),
                ('party', models.TextField(help_text='Party alignment of candidate')),
            ],
        ),
        migrations.CreateModel(
            name='Utterance',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('seqid', models.IntegerField(help_text='Sequence at which the utterance was made')),
                ('event', models.ForeignKey(to='debates.Event', help_text='Event utterance was spoken at')),
                ('sentence', models.ForeignKey(to='javanlp.Sentence', help_text='Actual text of the utterance')),
                ('speaker', models.ForeignKey(to='debates.Speaker', help_text='Speaker of utterance')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='speakers',
            field=models.ManyToManyField(to='debates.Speaker', help_text='When did the candidates speak?'),
        ),
    ]
