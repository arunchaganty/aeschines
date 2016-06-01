from django.core.management.base import BaseCommand, CommandError

from collections import Counter
import csv
import sys

from twit.models import Tweet
from twit.util import identify_stance, RowObjectFactory

class DataProcessingCommand(BaseCommand):
    """A command that processes data, from input to output, either using a table or using the output.
    Each processing function is wrapped in a transaction.
    """
    help = __doc__

    def add_arguments(self, parser):
        parser.add_argument('--input', type=str, help="An optional input file (use '-' for stdin)")
        parser.add_argument('--output', type=str, help="An optional output file (use '-' for stdout)")

    def output_header(self):
        """Must define the schema of the output"""
        raise NotImplementedError()

    def process(self, istream):
        """
        Client must return ostream
        """
        raise NotImplementedError()

    def db_to_istream(self):
        raise NotImplementedError("Must define fn to create input stream from database")

    def ostream_to_db(self, ostream):
        raise NotImplementedError("Must define fn to load database from output stream")

    def file_to_istream(self, ifstream):
        """
        Returns row objects
        """
        reader = csv.reader(ifstream, delimiter='\t')
        header = next(reader)
        factory = RowObjectFactory(header)
        return map(factory.build, reader)

    def ostream_to_file(self, ofstream, ostream):
        """
        Returns row objects
        """
        writer = csv.writer(ofstream, delimiter='\t')
        writer.writerrow(self.output_header())
        for row in ostream:
            writer.writerrow(row)

    def handle(self, *args, **options):
        if options['input'] is not None:
            if options['input'] == "-":
                ifstream = sys.stdin
            else:
                ifstream = open(options['input'], 'r')
            istream = self.file_to_istream(ifstream)
        else:
            istream = self.db_to_istream()

        # Actually process the data.
        ostream = self.process(istream)

        if options['output'] is not None:
            if options['output'] == "-":
                ofstream = sys.stdout
            else:
                ofstream = open(options['output'], 'w')
            self.ostream_to_file(ofstream, ostream)
        else:
            self.ostream_to_db(ostream)
