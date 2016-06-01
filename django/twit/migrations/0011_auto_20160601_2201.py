# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twit', '0010_entitymention_entitystance_topicmention'),
    ]

    operations = [
        migrations.CreateModel(
            name='StanceTopicSummary',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('entity', models.TextField()),
                ('stance', models.FloatField(help_text='For/Neutral/Against')),
                ('topic', models.TextField()),
                ('count', models.BigIntegerField()),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.AlterField(
            model_name='entitystance',
            name='tweet',
            field=models.ForeignKey(to='twit.Tweet', related_name='stances'),
        ),
        migrations.AlterField(
            model_name='topicmention',
            name='tweet',
            field=models.ForeignKey(to='twit.Tweet', related_name='topics'),
        ),
    ]
