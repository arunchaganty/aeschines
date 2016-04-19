from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from itertools import islice
import sys
#import json

from twit.util import connect, stream_tweets
from twit.models import User, Tweet, Mention, UserMention


class Command(BaseCommand):
    """Scrape tweets from twitter and load into database."""
    help = __doc__

    def add_arguments(self, parser):
        import argparse
        parser.add_argument('--id_file', type=str, help="ID file that contains information about maximum ids used.")
        parser.add_argument('--output_file', type=FileType('a'), help="File that contains raw json tweet dump.")

    def handle(self, *args, **options):
        api = connect()

        for kw in KEYWORDS:
            with transaction.atomic():
                for tweet in islice(get_tweets(api, q=SEARCH_TEMPLATE.format(kw=kw), lang='en', result_type='recent', max_id=options['max_id']), MAX_TWEETS):
                    # Create a user object
                    User.from_json(tweet['user']).update_or_create()
                    tweet_, created = Tweet.from_json(tweet).get_or_create()
                    if created:
                        for entity in tweet['entities']['hashtags']:
                            Mention.from_json(entity, 'hashtag', tweet_).save()
                        for entity in tweet['entities']['user_mentions']:
                            UserMention.from_json(entity, tweet_).save()

