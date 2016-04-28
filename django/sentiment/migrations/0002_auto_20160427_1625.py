# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sentiment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entitymention',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False),
        ),
        migrations.AlterField(
            model_name='topicmention',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False),
        ),
    ]
