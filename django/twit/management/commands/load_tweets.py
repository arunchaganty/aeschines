from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

import sys
import json

from twit.models import User, Tweet, Retweet, Mention, UserMention

class Command(BaseCommand):
    """Scrape tweets from twitter and load into database."""
    help = __doc__

    def add_arguments(self, parser):
        import argparse
        parser.add_argument('--input', type=argparse.FileType('r'), help="Input file containing a json tweet on each line.")

    def handle(self, *args, **options):
        for line in options['input']:
            line = line.strip()
            if len(line) == 0: continue

            with transaction.atomic():
                tweet = json.loads(line)
                print(tweet['id']) # To keep track of progress.

                if Tweet.is_retweet(tweet):
                    Retweet.from_json(tweet).update_or_create()
                else:
                    # Create the tweet.
                    tweet_, created = Tweet.from_json(tweet).update_or_create()
                    # Update the entities
                    if created:
                        for entity in tweet['entities']['hashtags']:
                            Mention.from_json(entity, 'hashtag', tweet_).save()
                        for entity in tweet['entities']['user_mentions']:
                            UserMention.from_json(entity, tweet_).save()

