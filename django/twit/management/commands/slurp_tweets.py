#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Slurp tweets periodically and append into a file
"""
from itertools import islice
import sys
import csv
import json
import argparse
from twit.util import connect, slurp_tweets, TwitterHTTPError, RATE_LIMIT, RESULTS_PER_QUERY

import ipdb

from django.core.management.base import BaseCommand

def update_for_keyword(api, output, keyword, max_id, count):
    """
    Update file with tweets slurped from .
    """

    max_id_ = max_id
    idx = 0
    try:
        for idx, tweet in enumerate(islice(slurp_tweets(api, keyword, max_id), count)):
            max_id_ = tweet['id']
            output.write(json.dumps(tweet).replace('\n','').replace('\r','').strip() + "\n")
    except TwitterHTTPError as e:
        print(e) # Just print this as a warning and continue.

    return max_id_, idx != count-1

class IdFile(dict):
    """
    Stores a family of ids.
    """
    @staticmethod
    def read(fname):
        """Read id file"""
        with open(fname, 'r') as f:
            reader = csv.reader(f)

            header = next(reader)
            assert header == ['keyword', 'max_id', 'done']

            return IdFile({keyword.strip() : (int(max_id.strip()), done.strip() == 'True') for (keyword, max_id, done) in reader})

    def save(self, fname):
        """Write id file"""
        with open(fname, 'w') as f:
            writer = csv.writer(f)

            writer.writerow(['keyword', 'max_id', 'done'])
            for (keyword, (max_id, done)) in self.items():
                writer.writerow([keyword, max_id, done])

class Command(BaseCommand):
    """Slurp tweets from twitter and save into a file."""
    help = __doc__

    def add_arguments(self, parser):
        parser.add_argument('--id_file', type=str, help="ID file that contains information about the maximum ids used")
        parser.add_argument('--output', type=argparse.FileType('a'), default=sys.stdout, help="")

    def handle(self, *args, **options):
        id_file, output = options['id_file'], options['output']

        #ipdb.set_trace()
        # Read the id file
        ids = IdFile.read(id_file)

        api = connect()
        per_keyword_count = int(RATE_LIMIT * RESULTS_PER_QUERY / len(ids))
        print("Querying ~{} tweets per keyword for {} keywords".format(per_keyword_count, len(ids)))

        for keyword, (max_id, done) in ids.items():
            print("Querying for {}. Current max_id={}".format(keyword, max_id))
            if not done:
                max_id, done = update_for_keyword(api, output, keyword, max_id, per_keyword_count)
                ids[keyword] = (max_id, done)
            print("Done querying for {}. Current max_id={}".format(keyword, max_id))
            # save state
            ids.save(id_file)

