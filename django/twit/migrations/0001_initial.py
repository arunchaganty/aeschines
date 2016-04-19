# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import twit.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mention',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('type', models.CharField(help_text='Type of entity', max_length=16)),
                ('text', models.CharField(max_length=256)),
                ('doc_char_begin', models.IntegerField(help_text='Character offset in tweet')),
                ('doc_char_end', models.IntegerField(help_text='Character offset in tweet')),
            ],
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.BigIntegerField(help_text='Unique id that comes from Twitter', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(help_text='Time tweet was created')),
                ('text', models.CharField(help_text='Raw text context of tweet', max_length=256)),
                ('retweet_count', models.IntegerField(help_text='Count of retweets')),
                ('reply_to_id', models.IntegerField(default=-1, help_text='Reference to an existing tweet (may not be in database)')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigIntegerField(help_text='Unique id that comes from Twitter', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Full user name', max_length=512)),
                ('created_at', models.DateTimeField(help_text='Time tweet was created')),
                ('location', models.TextField(help_text='String description of location')),
                ('follower_count', models.IntegerField(default=0, help_text='Number of followers')),
                ('verified', models.BooleanField(help_text='Is the user verified')),
                ('time_zone', models.TextField(help_text='Timezone used by user')),
                ('description', models.TextField(help_text='Description of user')),
                ('status_count', models.IntegerField(help_text='Number of status updates by user')),
                ('friends_count', models.IntegerField(help_text='Number of friends')),
                ('screen_name', models.CharField(help_text='Short user name', max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='UserMention',
            fields=[
                ('mention_ptr', models.OneToOneField(auto_created=True, primary_key=True, to='twit.Mention', parent_link=True, serialize=False)),
                ('user_id', models.IntegerField(verbose_name=twit.models.User, help_text='User mentioned in the tweet')),
            ],
            bases=('twit.mention',),
        ),
        migrations.AddField(
            model_name='tweet',
            name='user',
            field=models.ForeignKey(to='twit.User'),
        ),
        migrations.AddField(
            model_name='mention',
            name='tweet',
            field=models.ForeignKey(to='twit.Tweet', help_text='Tweet containing this entity'),
        ),
    ]
