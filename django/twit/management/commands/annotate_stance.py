"""Annotate tweets with stance markers"""

from twit.models import Tweet
from twit.util import identify_stance

from . import DataProcessingCommand

class Command(DataProcessingCommand):
    """Annotate tweets with stance markers"""
    help = __doc__

    def process(self, istream):
        """
        Each element of istream is a tweet.
        Use the text as a marker.
        Return (id, text, score).
        Client must return (header, ostream)
        """
        for tweet in istream:
            stance = identify_stance(tweet.text.lower())
            for candidate, value in stance.items():
                yield [tweet.id, candidate, value, 1.0]

    def db_to_istream(self):
        return Tweet.objects.all()

    def output_header(self):
        return ["tweet_id", "entity", "stance", "score"]

    def ostream_to_db(self, ostream):
        raise NotImplementedError("Must define fn to load database from output stream")

