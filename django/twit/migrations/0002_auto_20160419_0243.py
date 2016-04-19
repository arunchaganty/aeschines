# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twit', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='follower_count',
            new_name='followers_count',
        ),
    ]
