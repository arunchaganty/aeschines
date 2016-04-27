from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

import sys
import json

from twit.models import User, Tweet, Mention, UserMention


class Command(BaseCommand):
    """Scrape tweets from twitter and load into database."""
    help = __doc__

    def add_arguments(self, parser):
        import argparse
        parser.add_argument('--input', type=argparse.FileType('r'), help="Input file containing a json tweet on each line.")

    def handle(self, *args, **options):
        with transaction.atomic():
            for line in options['input']:
                tweet = json.loads(line)
                # Create a user object
                User.from_json(tweet['user']).update_or_create()
                tweet_, created = Tweet.from_json(tweet).get_or_create()
                if created:
                    for entity in tweet['entities']['hashtags']:
                        Mention.from_json(entity, 'hashtag', tweet_).save()
                    for entity in tweet['entities']['user_mentions']:
                        UserMention.from_json(entity, tweet_).save()
