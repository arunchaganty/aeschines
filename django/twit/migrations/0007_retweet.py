# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twit', '0006_auto_20160419_0248'),
    ]

    operations = [
        migrations.CreateModel(
            name='Retweet',
            fields=[
                ('id', models.BigIntegerField(serialize=False, help_text='Unique id that comes from Twitter', primary_key=True)),
                ('created_at', models.DateTimeField(help_text='Time tweet was created')),
                ('tweet', models.ForeignKey(to='twit.Tweet')),
                ('user', models.ForeignKey(to='twit.User')),
            ],
        ),
    ]
