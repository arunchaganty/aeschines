# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twit', '0002_auto_20160419_0243'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='status_count',
            new_name='statuses_count',
        ),
    ]
