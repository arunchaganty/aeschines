from django.core.management.base import BaseCommand, CommandError
from javanlp.models import Sentence
from javanlp.util import annotate_document
from debates.models import Speaker, Event, Utterance

import datetime

import csv
import ipdb


class Command(BaseCommand):
    'Takes debate metadata from [meta] and transcript from [transcript], sends them through JavaNLP for annotations and then populates tables.'
    help = __doc__

    def add_arguments(self, parser):
        parser.add_argument('--meta', type=str, help="Path to file with metadata")
        parser.add_argument('--transcript', type=str, help="Path to a CSV with transcript")
        parser.add_argument('--server', type=str, default='localhost:9000', help="A JavaNLP annotation server endpoint")

    def parse_meta(self, fp):
        """
        Parse meta given filepath
        """
        lines = open(fp, 'r').readlines()

        name = lines[0].strip()
        location = lines[1].strip()
        date = lines[2].strip()
        date = datetime.datetime.strptime(date, "%B %d, %Y")

        name = name + " Debate " + date.strftime("%Y%m%d")
        event, _ = Event.objects.update_or_create(
            name = name,
            location = location,
            date = date)

        speakers = {}
        for line in lines[3:]:
            line = line.strip()
            name, party = line.split(',')
            _, last = name.split()

            speaker, _ = Speaker.objects.update_or_create(
                name = name,
                party = party)

            speakers[last.lower()] = speaker
            event.speakers.add(speaker)
        return event, speakers

    def parse_debate(self, event, speakers, fp, server):
        """
        Read all sentences in the debate.
        """
        with open(fp) as f:
            for seqid, speaker, utterance in csv.reader(f):
                seqid, speaker = int(seqid), speakers[speaker.lower()]
                docid = event.name.replace(" ","") + "_" + str(seqid)
                for idx, sentence in enumerate(annotate_document(docid, utterance, server)):
                    sentence.save()

                    u = Utterance(
                        event = event,
                        speaker = speaker,
                        seqid = seqid,
                        sentence_seqid = idx,
                        sentence = sentence)
                    u.save()


    def handle(self, *args, **options):
        assert options['meta'] is not None
        assert options['transcript'] is not None
        assert options['server'] is not None

        event, speakers = self.parse_meta(options['meta'])
        self.parse_debate(event, speakers, options['transcript'], options['server'])

