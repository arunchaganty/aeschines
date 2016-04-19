# -*- coding: utf-8 -*-
"""
Various utilities for interfacing with Twitter
"""

from twitter import Twitter, OAuth
from twitter.api import TwitterHTTPError
from twit.settings import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET

SEARCH_TEMPLATE = '{kw} -RT -filter:media -filter:links'
RATE_LIMIT = 180
RESULTS_PER_QUERY = 100
DEBUG = True

def connect():
    """Connect to twitter"""
    return Twitter(
        auth=OAuth(
            consumer_key=CONSUMER_KEY,
            consumer_secret=CONSUMER_SECRET,
            token=ACCESS_KEY,
            token_secret=ACCESS_SECRET))

def stream_tweets(api, keyword, max_id = -1):
    """
    Implements the max_id, max_id logic to create an infinte stream of
    tweets for a given search query.
    """
    # Set the max_id argument (if not already set in the arguments)

    while True:
        # Make actual API call
        ret = api.search.tweets(
            q=SEARCH_TEMPLATE.format(kw=keyword),
            max_id=max_id,
            count=RESULTS_PER_QUERY,
            lang='en',
            result_type='recent')

        lst = ret['statuses']
        if DEBUG:
            print("Received {} tweets.".format(len(lst)))
        if len(lst) == 0: break

        yield from lst

        # Update max_id for next call
        max_id = lst[-1]['id'] - 1

