from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

import csv
import sys
import json
import gzip
from tqdm import tqdm

from twit.models import User, Tweet, Retweet, Mention, UserMention

class Command(BaseCommand):
    """Scrape tweets from twitter and load into database."""
    help = __doc__

    def add_arguments(self, parser):
        import argparse
        parser.add_argument('--input', type=str, required=True, help="Path to a file containing a json tweet on each line.")
        parser.add_argument('--output-prefix', type=str, default='twit_', help="Forms the root of several output file names")

    def handle(self, *args, **options):
        # Open the file
        input_fname = options['input']
        if input_fname.endswith('.gz'):
            input_handler = gzip.open
        else:
            input_handler = open

        seen_tweets = set()
        users_map = {}

        users_fname, tweets_fname, retweets_fname = ["%s%s.tsv.gz"%(options['output_prefix'], x) for x in ['users', 'tweets', 'retweets']]

        with gzip.open(users_fname, 'at') as users_f,\
                gzip.open(tweets_fname, 'at') as tweets_f,\
                gzip.open(retweets_fname, 'at') as retweets_f,\
                input_handler(input_fname, 'rt') as f:
            # Create writers
            users, tweets, retweets = [csv.writer(f, delimiter='\t') for f in (users_f, tweets_f, retweets_f)]
            users.writerow(User.from_json_to_tsv_header())
            retweets.writerow(Retweet.from_json_to_tsv_header())
            tweets.writerow(Tweet.from_json_to_tsv_header())

            for line in tqdm(f):
                line = line.strip() # decode line
                if len(line) == 0: continue # Ignore empty lines
                tweet = json.loads(line)

                users_map[tweet['user']['id']] = User.from_json_to_tsv(tweet['user'])
                if Tweet.is_retweet(tweet):
                    if tweet['retweeted_status']['id'] not in seen_tweets:
                        tweets.writerow(Tweet.from_json_to_tsv(tweet['retweeted_status']))
                        seen_tweets.add(tweet['retweeted_status']['id'])
                    retweets.writerow(Retweet.from_json_to_tsv(tweet))
                else:
                    tweets.writerow(Tweet.from_json_to_tsv(tweet))
                seen_tweets.add(tweet['id'])

            for user in users_map.values():
                users.writerow(user)
