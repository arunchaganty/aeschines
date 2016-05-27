# -*- coding: utf-8 -*-
"""
Various utilities for interfacing with Twitter
"""

import re
from collections import Counter
#import ipdb

from twitter import Twitter, OAuth, TwitterStream
from twit.settings import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET, STREAM_CONSUMER_KEY, STREAM_CONSUMER_SECRET, STREAM_ACCESS_KEY, STREAM_ACCESS_SECRET


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

def connect_stream():
    """Connect to twitter"""
    return TwitterStream(
        auth=OAuth(
            consumer_key=STREAM_CONSUMER_KEY,
            consumer_secret=STREAM_CONSUMER_SECRET,
            token=STREAM_ACCESS_KEY,
            token_secret=STREAM_ACCESS_SECRET))


def slurp_tweets(api, keyword, max_id = -1, since_id = -1):
    """
    Implements the max_id, max_id logic to create an infinte stream of
    tweets for a given search query.
    """
    # Set the max_id argument (if not already set in the arguments)

    while True:
        # Make actual API call
        ret = api.search.tweets(
            q=SEARCH_TEMPLATE.format(kw=keyword),
            since_id=since_id,
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

def tweet_filter(tweet):
    """
    Filter tweets to only be:
        - English
        - Contain no media
    """
    try:
        if tweet['lang'] != 'en': return False
        if 'media' in tweet['entities'] and len(tweet['entities']['media']) > 0: return False
        #if 'urls' in tweet['entities'] and len(tweet['entities']['urls']) > 0: return False
        return True
    except KeyError:
        return False

def stream_tweets(api, keywords):
    """
    Implements the max_id, max_id logic to create an infinte stream of
    tweets for a given search query.
    """
    # Set the max_id argument (if not already set in the arguments)

    # Make actual API call
    return filter(tweet_filter, api.statuses.filter(track=",".join(keywords),))
    #return filter(tweet_filter, api.statuses.sample())


def identify_issues(text):
    """
    Identify any issues mentioned in a span of text according to a simple lexicon.

    @text:str
    @returns:Counter - containing counts of how many issues occur in each tweet.
    """
    issues = {
        "Energy and Environment": ['energy', 'oil', 'coal', 'miner?s', 'fracking', 'environment', 'greenhouse gas(es)?',],
        "Crime": ['crime', 'arrests?', 'body cameras', 'police brutality', 'prison reform'],
        "Religion": ['religions?', 'religious'],
        "Government Reform and Campaign Finance": ['government reform', "super pac", "pac", "campaign contributions?"],
        "Jobs": ['jobs', 'unemployment'],
        "Drugs": ['drugs'],
        "Gun Control": ['gun control', 'guns?', 'nra'],
        "Immigration": ['immigration', 'border patrol', 'border', 'deportation', 'immigrants?'],
        "Free Trade": ['free trade', 'trade', 'nafta', 'tpp'],
        "Foreign policy": ['foreign policy'],
        "War & Peace": ['iraq war', 'peace'],
        "Infrastructure & Technology": ['infrastructure',],
        # "Tax Reform": ['tax', 'taxes', 'tax reform'],
        # "Civil Rights": ['civil rights', 'equal rights'],
        "Health Care": ['health care', 'healthcare'],
        # "Families & Children": ['families', 'children'],
        "Welfare & Poverty": ['social welfare'],
        "Criminal Justice": ['criminal justice'],
        "Homeland Security": ['homeland security',],
        # "Corporations": ['corporations'],
        # "Education": ['education'],
        "Abortion": ['abortion', 'planned parenthood'],
        "Gay rights": ['lgbt', 'gay rights', 'lesbian', 'bisexual', 'transgender'],
    }

    counts = Counter()
    matches_at_least_one_issue = False
    for issue, words in issues.items():
        regex = r"\b(%s)\b" % ('|'.join(words))
        if re.search(regex, text) is not None:
            counts[issue] += 1
            matches_at_least_one_issue = True
    if not matches_at_least_one_issue:
        counts["None"] += 1
    return counts
