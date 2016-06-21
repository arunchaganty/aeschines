"""Annotate tweets with issues they contain"""

from twit.models import Tweet
from twit.util import identify_issues, queryset_iterator
from twit.tqdm import tqdm

from . import DataProcessingCommand

class Command(DataProcessingCommand):
    """Annotate tweets with stance markers"""
    help = __doc__

    def process(self, istream, count=None):
        """
        Each element of istream is a tweet.
        Use the text as a marker.
        Return (id, text, score).
        Client must return (header, ostream)
        """
        if count is not None:
            istream = tqdm(istream, total=count)
        for tweet in istream:
            for issue in identify_issues(tweet.text.lower()):
                yield [tweet.id, issue, 1.0]

    def db_to_istream(self):
        return queryset_iterator(Tweet.objects.all())

    def db_istream_count(self):
        return Tweet.objects.count()

    def output_header(self):
        return ["tweet_id", "topic", "score"]

    def ostream_to_db(self, ostream):
        raise NotImplementedError("Must define fn to load database from output stream")

