#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Stream tweets continuous and append into a (gzipped) file
"""
import sys
import csv
import gzip
import json
import argparse
from twit.util import connect_stream, stream_tweets, TwitterHTTPError

from django.core.management.base import BaseCommand

def read_keywords(fname):
    """Read id file"""
    with open(fname, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        assert header == ['keyword']
        return list(row[0] for row in reader)

class Command(BaseCommand):
    """Slurp tweets from twitter and save into a file."""
    help = __doc__

    def add_arguments(self, parser):
        parser.add_argument('--keywords_file', type=str, help="File that contains information about keywords")
        parser.add_argument('--output', type=str, default='tweet_stream.gz', help="Path to save output to.")

    def handle(self, *args, **options):
        keywords_file, output_fname = options['keywords_file'], options['output']
        keywords = read_keywords(keywords_file)

        api = connect_stream()

        with gzip.open(output_fname, 'ab') as output:
            for tweet in stream_tweets(api, keywords):
                print(tweet['id'])
                output.write(bytes(json.dumps(tweet).replace('\n','').replace('\r','').strip() + "\n", 'utf-8'))

