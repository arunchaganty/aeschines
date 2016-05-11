# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twit', '0007_retweet'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='favorite_count',
            field=models.IntegerField(default=0, help_text='Count of favorites'),
        ),
    ]
