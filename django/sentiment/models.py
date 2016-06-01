"""
Models to capture sentiment
"""
from django.db import models
from twit.models import Tweet

class EntityMention(models.Model):
    """
    Identifies a mention of an entity within a tweet.
    """
    tweet = models.ForeignKey(Tweet)
    doc_char_begin = models.IntegerField()
    doc_char_end = models.IntegerField()
    gloss = models.TextField()
    best_entity = models.TextField()

    def __str__(self):
        return self.best_entity

    def __repr__(self):
        return "[Entity: {}]".format(self.best_entity)

class EntityStance(models.Model):
    """
    Identifies the purported stance of the specified entity.
    """
    tweet = models.ForeignKey(Tweet)
    entity = models.TextField(help_text='Entity with stance')
    stance = models.FloatField(help_text='Stance value')
    score = models.FloatField(help_text='Confidence of stance value')

    def __str__(self):
        return "{} {:.2f}".format(self.entity, self.stance)

    def __repr__(self):
        return "[Stance: {}={:.2f}]".format(self.entity, self.stance)

class TopicMention(models.Model):
    """
    Identifies which topic the tweet falls into.
    """
    tweet = models.ForeignKey(Tweet)
    topic = models.TextField(help_text='Description of a topic.')
    score = models.FloatField(help_text='Confidence of class')

    def __str__(self):
        return "{}".format(self.topic)

    def __repr__(self):
        return "[Topic: {}]".format(self.topic)


