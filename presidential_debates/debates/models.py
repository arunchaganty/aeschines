from django.db import models
from javanlp.models import Sentence

class Speaker(models.Model):
    """
    A speaker at a debate.
    """
    name = models.TextField(help_text="Name of candidate")
    # HACK: this might actually be on a per election basis.
    party = models.TextField(help_text="Party alignment of candidate")

class Event(models.Model):
    """
    Represents a particular speaking event (could be a speech or debate).
    """
    name = models.TextField(help_text='Name of the speaking event')
    date = models.DateField(help_text='When was the event?')
    speakers = models.ManyToManyField(Speaker, help_text='When did the candidates speak?')

class Utterance(models.Model):
    """
    Represents all the metadata around an utterance.
    """
    event = models.ForeignKey(Event, help_text='Event utterance was spoken at')
    speaker = models.ForeignKey(Speaker, help_text='Speaker of utterance')
    seqid = models.IntegerField(help_text='Sequence at which the utterance was made')
    sentence = models.ForeignKey(Sentence, help_text='Actual text of the utterance')

