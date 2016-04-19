# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import twit.models


class Migration(migrations.Migration):

    dependencies = [
        ('twit', '0004_auto_20160419_0246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='reply_to_id',
            field=models.BigIntegerField(default=-1, help_text='Reference to an existing tweet (may not be in database)'),
        ),
        migrations.AlterField(
            model_name='usermention',
            name='user_id',
            field=models.BigIntegerField(help_text='User mentioned in the tweet', verbose_name=twit.models.User),
        ),
    ]
