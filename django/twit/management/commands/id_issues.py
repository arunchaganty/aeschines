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
        parser.add_argument('--issues_dict', type=argparse.FileType('r'), help="Input file containing a issues and keywords corresponding to them.")

    def handle(self, *args, **options):
        for line in options['input']:
            for tweet in Tweet.objects.all():
                print(tweet) # do magic
