# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('javanlp', '0002_auto_20151105_2216'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sentiment',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('sentiment_value', models.IntegerField(help_text='sentiment on a -1 to 1 scale')),
            ],
        ),
        migrations.AlterField(
            model_name='sentence',
            name='doc_id',
            field=models.BigIntegerField(),
        ),
        migrations.AddField(
            model_name='sentiment',
            name='sentence',
            field=models.ForeignKey(to='javanlp.Sentence'),
        ),
    ]
