from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

import sys
import json

from twit.models import User, Tweet, Mention, UserMention
from javanlp.models import Sentence, Sentiment
from javanlp.util import AnnotationException, annotate_document_with_sentiment


class Command(BaseCommand):
    """Annotate tweets and load into database."""
    help = __doc__

    #def add_arguments(self, parser):
    #    import argparse
    #    parser.add_argument('--input', type=argparse.FileType('r'), help="Input file containing a json tweet on each line.")

    def handle(self, *args, **options):
        for tweet in Tweet.objects.all():
            if Sentence.objects.filter(doc_id = tweet.id).exists(): continue
            try:
                with transaction.atomic():
                    for sentence, sentiment in annotate_document_with_sentiment(tweet.id, tweet.text):
                        sentence.save()
                        sentiment.sentence = sentence
                        sentiment.save()
            except AnnotationException:
                pass # Couldn't annotate this sentence...
