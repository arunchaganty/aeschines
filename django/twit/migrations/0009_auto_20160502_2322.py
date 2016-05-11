# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twit', '0008_tweet_favorite_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='description',
            field=models.TextField(help_text='Description of user', null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.TextField(help_text='String description of location', null=True),
        ),
    ]
