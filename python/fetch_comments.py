#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Read twitter for comments
"""

from urllib.parse import unquote
import itertools as it
import csv
import sys
import json

from twitter import *
import props

def connect():
    t = Twitter(
        auth=OAuth(
            consumer_key=props.CONSUMER_KEY,
            consumer_secret=props.CONSUMER_SECRET,
            token=props.ACCESS_KEY,
            token_secret=props.ACCESS_SECRET))
    return t

def connect_stream():
    t = TwitterStream(
        auth=OAuth(
            consumer_key=props.CONSUMER_KEY,
            consumer_secret=props.CONSUMER_SECRET,
            token=props.ACCESS_KEY,
            token_secret=props.ACCESS_SECRET))
    return t

KEYWORDS = [
    'Hillary Clinton',
    'Bernie Sanders',
    'Donald Trump',
    'Ted Cruz',
    'John Kaisch',
    ]
SEARCH_TEMPLATE = '{kw} -RT -filter:media -"... http"'

def get_tweets(api, **kwargs):
    """
    Implements the max_id, since_id logic to slurp all tweets for a
    given search query.
    """
    CNT = 100

    ret = api.search.tweets(count=CNT, **kwargs)
    print(ret['search_metadata']['refresh_url'])
    lst = ret['statuses']
    while len(lst) > 0:
        yield from lst
        max_id = lst[-1]['id'] - 1
        ret = api.search.tweets(count=CNT, max_id=max_id, **kwargs)
        print(ret['search_metadata']['refresh_url'])
        lst = ret['statuses']

def do_command(args):
    api = connect()
    MAX_TWEETS = 80 * 100

    writer = csv.writer(args.output)

    writer.writerow(["id", "screen_name", "txt"])
    for kw in KEYWORDS:
        for tweet in it.islice(get_tweets(api, q=SEARCH_TEMPLATE.format(kw=kw)), MAX_TWEETS):
            id, screen_name, txt = tweet['id'], tweet['user']['screen_name'], unquote(tweet['text'])
            txt = txt.replace('\n', ' ').strip()
            writer.writerow([id, screen_name, txt])

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser( description='' )
    parser.add_argument('--input', type=argparse.FileType('r'), default=sys.stdin, help="")
    parser.add_argument('--output', type=argparse.FileType('w'), default=sys.stdout, help="")
    parser.set_defaults(func=do_command)

    #subparsers = parser.add_subparsers()
    #command_parser = subparsers.add_parser('command', help='' )
    #command_parser.set_defaults(func=do_command)

    ARGS = parser.parse_args()
    ARGS.func(ARGS)
