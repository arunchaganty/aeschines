from django.core.management.base import BaseCommand, CommandError

from collections import Counter
import csv
import sys

from twit.models import Tweet
from twit.util import identify_issues

class Command(BaseCommand):
    """Scrape tweets from twitter and load into database."""
    help = __doc__

    def add_arguments(self, parser):
        import argparse
        parser.add_argument('--input', default=None, type=str, help="An optional input file containing columns [id, text] that will be read instead of the database.")
        parser.add_argument('--output', default=sys.stdout, type=argparse.FileType('w'), help="Where the output is written to.")
        parser.add_argument('--write-output', action='store_true', default=False, help="Will write [id,text,issues] to output if set.")

    def handle(self, *args, **options):
        if options['input'] is not None:
            with open(options['input']) as f:
                reader = csv.reader(f, delimiter='\t')
                header = next(reader)
                assert header == ["id", "text"]

                tweets = list(reader)
        else: 
            tweets = map(lambda t: (t.id, t.text), Tweet.objects.all())
        writer = csv.writer(options['output'], delimiter="\t") if options['write_output'] else None
        if writer is not None:
            writer.writerow(['id', 'text', 'issues'])

        counts = Counter()
        print("Building counts by issue")
        for id, text in tweets:
            issues = identify_issues(text.lower())
            if writer is not None:
                writer.writerow([id, text, ",".join(issues.keys())])
            counts.update(issues)

        print("Issues referenced most often in descending order")
        for issue, count in counts.most_common():
            print("%4d %s" % (count, issue))
