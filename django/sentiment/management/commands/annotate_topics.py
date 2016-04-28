from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

import sys
import csv

import ipdb

from twit.models import User, Tweet, Mention, UserMention
from javanlp.models import Sentence, Sentiment
from collections import Counter

def extract_candidates(text):
    mapping = {
        'Hillary Clinton' : 'HC',
        'Bernie Sanders ' : 'BS',
        'Donald Trump' : 'DT',
        'Ted Cruz' : 'TC',
        }
    ret = []
    for key, value in mapping.items():
        for keyword in key.lower().split():
            if keyword in text.lower():
                ret.append(value)
                break
    return ret

def extract_topics(sentence):
    ret = []
    start_idx = None
    for idx, tag in enumerate(sentence.pos_tags):
        if tag.startswith('NN') and start_idx is None:
            start_idx = idx
        elif not tag.startswith('NN') and start_idx is not None:
            topic = " ".join(sentence.words[start_idx:idx]).lower()
            ret.append(topic)
            start_idx = None
    return ret

def test_extract_topics():
    # I get that Trump allows for a good transference of anger, but Ted Cruz has better policies, acted as a conservative and can fix econ faster 
    sentence = Sentence.objects.get(id=2666)
    topics = extract_topics(sentence)
    #ipdb.set_trace()
    assert len(topics) > 1

class Command(BaseCommand):
    """Annotate tweets and load into database."""
    help = __doc__

    def add_arguments(self, parser):
        import argparse
        parser.add_argument('--output', type=argparse.FileType('w'), help="File describing text")

    def handle(self, *args, **options):
        topic_counts = Counter()
        topic_sentiment = Counter()

        for sentence in Sentence.objects.all():
            sentiment = sentence.sentiment_set.first().sentiment_value
            candidates = extract_candidates(sentence.gloss)
            topics  = extract_topics(sentence)

            for topic in topics:
                topic_counts[topic] += 1
                topic_sentiment[topic] += sentiment

                for candidate in candidates:
                    topic_counts[topic, candidate] += 1
                    topic_sentiment[topic, candidate] += sentiment

        # By construction, in order
        key_topics = [key for key, _ in topic_counts.most_common() if isinstance(key, str)]
        writer = csv.writer(options['output'])
        writer.writerow(['topic', 'BS', 'DT', 'TC', 'HC', 'total', 'total_counts'])
        for key in key_topics:
            writer.writerow(
                [key,] +
                ['%.2f'%(topic_sentiment[(key,c)] / (topic_counts[(key,c)] + 0.1)) for c in ['BS', 'DT', 'TC', 'HC']] + # Small smoothing.
                ['%.2f'%(topic_sentiment[key] / topic_counts[key]), topic_counts[key]])

