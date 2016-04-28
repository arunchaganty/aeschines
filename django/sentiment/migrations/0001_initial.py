# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twit', '0007_retweet'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntityMention',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('doc_char_begin', models.IntegerField()),
                ('doc_char_end', models.IntegerField()),
                ('gloss', models.TextField()),
                ('best_entity', models.TextField()),
                ('tweet', models.ForeignKey(to='twit.Tweet')),
            ],
        ),
        migrations.CreateModel(
            name='TopicMention',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('doc_char_begin', models.IntegerField()),
                ('doc_char_end', models.IntegerField()),
                ('gloss', models.TextField()),
                ('best_entity', models.TextField()),
                ('tweet', models.ForeignKey(to='twit.Tweet')),
            ],
        ),
    ]
