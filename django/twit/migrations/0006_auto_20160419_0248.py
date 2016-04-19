# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twit', '0005_auto_20160419_0247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='reply_to_id',
            field=models.BigIntegerField(help_text='Reference to an existing tweet (may not be in database)', default=-1, null=True),
        ),
    ]
