from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

import itertools as it
import sys
#import json

from twitter import Twitter, OAuth
from twit.settings import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET
from twit.models import User, Tweet, Mention, UserMention

def connect():
    t = Twitter(
        auth=OAuth(
            consumer_key=CONSUMER_KEY,
            consumer_secret=CONSUMER_SECRET,
            token=ACCESS_KEY,
            token_secret=ACCESS_SECRET))
    return t

KEYWORDS = [
    'Hillary Clinton',
    'Bernie Sanders',
    'Donald Trump',
    'Ted Cruz',
    'John Kaisch',
    ]
SEARCH_TEMPLATE = '{kw} -RT -filter:media -filter:links'
RATE_LIMIT = 180
RESULTS_PER_QUERY = 100
MAX_TWEETS = 300 #int(RATE_LIMIT * RESULTS_PER_QUERY / len(KEYWORDS)) # Limited to 100 tweets per request, and 180 requests.

def get_tweets(api, **kwargs):
    """
    Implements the max_id, max_id logic to slurp all tweets for a
    given search query.
    """
    kwargs['max_id'] = kwargs.get('max_id', -1)
    ret = api.search.tweets(count=RESULTS_PER_QUERY, **kwargs)
    print(ret['search_metadata'].get('refresh_url', ""))
    lst = ret['statuses']
    print("Got %d results" % len(lst))
    while len(lst) > 0:
        yield from lst
        kwargs['max_id'] = lst[-1]['id'] - 1
        ret = api.search.tweets(count=RESULTS_PER_QUERY, **kwargs)
        print(ret['search_metadata'].get('refresh_url', ""))
        lst = ret['statuses']
        print("Got %d results" % len(lst))

class Command(BaseCommand):
    """Scrape tweets from twitter and load into database."""
    help = __doc__

    def add_arguments(self, parser):
        parser.add_argument('--max_id', type=int, default=-1, help="Maximum id to use")

    def handle(self, *args, **options):
        api = connect()

        for kw in KEYWORDS:
            with transaction.atomic():
                for tweet in it.islice(get_tweets(api, q=SEARCH_TEMPLATE.format(kw=kw), lang='en', result_type='recent', max_id=options['max_id']), MAX_TWEETS):
                    # Create a user object
                    User.from_json(tweet['user']).update_or_create()
                    tweet_, created = Tweet.from_json(tweet).get_or_create()
                    if created:
                        for entity in tweet['entities']['hashtags']:
                            Mention.from_json(entity, 'hashtag', tweet_).save()
                        for entity in tweet['entities']['user_mentions']:
                            UserMention.from_json(entity, tweet_).save()

