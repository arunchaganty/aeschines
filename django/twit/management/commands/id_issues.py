from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from collections import Counter
import json
import re
import sys

from twit.models import User, Tweet, Retweet, Mention, UserMention

class Command(BaseCommand):
    """Scrape tweets from twitter and load into database."""
    help = __doc__

    def add_arguments(self, parser):
        import argparse
        # parser.add_argument('--issues_dict', type=argparse.FileType('r'), help="Input file containing a issues and keywords corresponding to them.")

    def handle(self, *args, **options):
        issues = {
            "Free Trade": "free trade|trade",
            "Energy & Oil": "energy|oil",
            "Jobs": "jobs",
            "Environment": "environment",
            "Corporations": "corporations",
            "Tax Reform": "tax|taxes|tax reform",
            "Tax Reform": "tax reform|tax|taxes",
            "Government Reform": "government reform",
            "Infrastructure & Technology": "infrastructure|technology",
            "Education": "education",
            "Health Care": "health care|healthcare|obamacare",
            "Civil Rights": "civil rights|equal rights",
            "Families & Children": "families|children",
            "Religion": "religion",
            "Criminal Justice": "criminal justice",
            "Gun Control": "gun control|gun|guns",
            "Welfare & Poverty": "welfare|poverty",
            "Crime": "crime",
            "Drugs": "drugs",
            "Immigration": "immigration|border patrol|border",
            "Foreign policy": "foreign policy",
            "War & Peace": "war|peace",
            "Homeland Security": "homeland security|dhs",
        }
        counts = Counter()

        print("Building counts by issue")
        for i, tweet in enumerate(Tweet.objects.all()):
            text = tweet.text.lower()
            for issue, regex in issues.items():
                if re.search(regex, text) is not None:
                    counts[issue] += 1
        print("Issues referenced most often in descending order")
        for issue, count in counts.most_common():
            print("%4d %s" % (count, issue))
