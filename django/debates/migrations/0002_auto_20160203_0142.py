# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debates', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.TextField(default='', help_text='Where was the event?'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='utterance',
            name='sentence_seqid',
            field=models.IntegerField(default=-1, help_text='Sequence in the utterance'),
            preserve_default=False,
        ),
    ]
