from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from collections import Counter
import json
import re
import sys

from twit.models import User, Tweet, Retweet, Mention, UserMention
from twit.util import identify_issues

class Command(BaseCommand):
    """Scrape tweets from twitter and load into database."""
    help = __doc__

    def add_arguments(self, parser):
        import argparse
        # parser.add_argument('--issues_dict', type=argparse.FileType('r'), help="Input file containing a issues and keywords corresponding to them.")

    def handle(self, *args, **options):
        counts = Counter()

        print("Building counts by issue")
        for tweet in Tweet.objects.all():
            text = tweet.text.lower()
            counts.update(identify_issues(text))

        print("Issues referenced most often in descending order")
        for issue, count in counts.most_common():
            print("%4d %s" % (count, issue))
